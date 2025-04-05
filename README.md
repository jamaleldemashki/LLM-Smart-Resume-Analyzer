# 🧠 Smart Resume Analyzer

**Built with ❤️ by Jamal Eldemashki**

> This project was created as a learning experience to explore **LLM models**, run **LLaMA locally** with **Ollama**, and build interactive web apps using **Streamlit**.

---

## 🚀 Features

✅ Upload your resume as a **PDF**  
✅ Paste a **job description**  
✅ Get an **AI-generated match score**  
✅ See **strengths, weaknesses & improvement suggestions**  
✅ Generate powerful **bullet points for your cover letter**  
✅ Optionally generate a **full, personalized cover letter**

---

## 🖼️ Demo

📌 _Coming soon: Add a GIF or screenshot here_

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Engine**: [LLaMA 2](https://ollama.com/library/llama2) via [Ollama](https://ollama.com/)
- **PDF Parsing**: `PyMuPDF` (`fitz`)
- **Local API**: Ollama's localhost endpoint

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/smart-resume-analyzer.git
cd smart-resume-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit requests PyMuPDF
```

### 3.

Install Ollama & Pull LLaMA Model
Download Ollama from https://ollama.com
Then run:

```bash
ollama run llama2
```

## 🧪 Run the App

```bash
streamlit run app.py
```

Your browser will open the app automatically.

## 📁 Sample Files

To test the app, you can use the included sample files in the samples/ folder:

Dummy_resume.pdf — Dummy resume

DummyJobDescription.txt — Matching job description

## ✨ Author

👤 Jamal Eldemashki
