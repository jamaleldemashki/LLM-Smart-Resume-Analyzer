import streamlit as st 
import requests
import fitz #PyMuPDF


# PDF Text Extractor
def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

# LLM Call (Ollama)
def call_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# Streamlit Page Config
st.set_page_config(page_title="Smart Resume Analyzer", page_icon="🧠", layout="wide")
st.markdown(
    """
    <style>
    .main{
        background-color: #f9f9f9;
    }
    .stTextArea, .stFileUploader, .stButton {
        margin-nottom: 20px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Stramlit UI

st.title("🧠 Smart Resume Analyzer")
st.subheader("Analyze your resume, get feedback, and generate cover letters with LLaMa")
st.markdown("---")

# Upload Resume PDF
col1, col2 = st.columns([1, 2])
with col1:
    uploaded_resume = st.file_uploader("📄 Upload Your Resume (PDF)", type="pdf")
with col2:
    job_description = st.text_area("💼 Paste Job Description")

generate_full_cover = st.checkbox("📝 Also generate a full Cover Letter", value=True)


if uploaded_resume and job_description and st.button("🚀 Analyze Resume"):
    resume_text = extract_text_from_pdf(uploaded_resume)
    
    with st.spinner("Analyzing with LLaMa..."):
        # Promot 1_ resume Match & Feedback
        analysis_prompt = f"""
        You are an expert resume revierwer.
        
        RESUME:
        {resume_text}
        
        JOB DESCRIPTION:
        {job_description}
        
        TASK:
        1. Give me a match score between 0 and 100 (You must show a number, and nothing else). 
        2. Highlight strenghts and weaknesses of this resume.
        3. Suggest improvments to better match the job description.
        4. In Taks 2 and 3 avoid duplicate or mentioning the same points twice.
        """
        analysis_response = call_ollama(analysis_prompt)
        
        # Prompt 2: Cover Letter Bullet Points
        cover_prompt = f"""
        Based on the resume and job description below, generate 4-5 strong bullet points
        that the candidate can include in a cover letter to make a great first impression. Each bullet point on a new line.
        
        RESUME:
        {resume_text}
        
        JOB DESCRIPTION:
        {job_description}
        """
        cover_response = call_ollama(cover_prompt)
        
        # Prompt 3: Full cover Letter
        full_cover_prompt = f"""
        Using the resume and job description, write a professional and personalised full cover letter.
        Address the hiring manager, highlight the most relevant experience, and keep it clear and impactful.
        
        RESUME:
        {resume_text}
        
        JOB DESCRIPTION:
        {job_description}
        """
        
        full_cover_letter = call_ollama(full_cover_prompt)
        
        # Display Results
        st.markdown("### 📊 Resume Analysis")
        st.write(analysis_response)
        
        st.markdown("### 📝 Cover Letter Bullet Points")
        # Split by line and display only lines that look like bullet points
        for line in cover_response.splitlines():
            if line.strip().startswith("-") or line.strip().startswith("•"):
                st.markdown(f"- {line.strip()[1:].strip()}")

        
        if full_cover_letter:
            st.markdown("## ✉️ Full Cover Letter")
            st.code(full_cover_letter, language="markdown")