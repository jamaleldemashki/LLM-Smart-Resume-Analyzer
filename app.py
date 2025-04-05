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

# Stramlit UI

st.title("🧠 Smart Resume Analyzer")

st.markdown("### 📄 Upload Your Resume (PDF)")
uploaded_resume = st.file_uploader("Upload a PDF file", type="pdf")

st.markdown("### 💼 Paste Job Description")
job_description = st.text_area("Job Description")

if uploaded_resume and job_description and st.button("Analyze"):
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
        
        # Display Results
        st.markdown("### 📊 Resume Analysis")
        st.write(analysis_response)
        
        st.markdown("### 📝 Cover Letter Bullet Points")
        st.write(cover_response)