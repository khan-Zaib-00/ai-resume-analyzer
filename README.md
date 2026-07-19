# AI Resume Analyzer & Career Coach

Welcome to the **AI Resume Analyzer & Career Coach**, a powerful tool built with Python, Streamlit, and LangChain that leverages Large Language Models (LLMs) to help candidates optimize their resumes and prepare for their dream jobs.

# Features

* ATS Match Score: Calculates a similarity score between your resume and a target job description using Sentence Transformers.
* Skill Extraction & Missing Skills: Identifies the technical and soft skills you have, and highlights what you're missing for the target job.
* Resume Analysis: Provides expert HR feedback on formatting, strengths, and areas for improvement.
* Interview Prep: Generates 5 tailored, challenging interview questions with answering tips based on your profile.
* Cover Letter Generator: Writes a professional, tailored cover letter in seconds.
* LinkedIn Summary: Crafts an engaging "About" section for your LinkedIn profile.
* Learning Roadmap: Gives you a step-by-step guide to acquiring the skills you're currently missing.

#  Tech Stack

* *Frontend: [Streamlit](https://streamlit.io/)
* *AI/LLM: [Groq API](https://groq.com/) (using Llama-3) & [LangChain](https://www.langchain.com/)
* *Embeddings: [Sentence Transformers](https://sbert.net/) (HuggingFace)
* *Data Processing: PyPDF2, Pandas
* *Visualization: Plotly

# How to Run Locally

# Prerequisites
You will need Python installed on your system and a free Groq API Key (get it from [console.groq.com](https://console.groq.com/)).

# Installation Steps

1. Clone the repository:
   bash
   git clone https://github.com/your-username/ai_resume_analyzer.git
   cd ai_resume_analyzer
   

2. Install required packages:
   bash
   pip install -r requirements.txt
   

3. Set up Environment Variables:
   GROQ_API_KEY=your_groq_api_key_here
   
   (Alternatively, you can paste the key directly into the app's sidebar when it runs).

4. Run the Application:
   bash
   python -m streamlit run app.py
   

# Contributing
Contributions are always welcome! Feel free to open a pull request or report an issue.

5. Author
# Khan Zaib
