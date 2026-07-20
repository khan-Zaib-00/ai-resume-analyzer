import streamlit as st
import os
from dotenv import load_dotenv
import plotly.graph_objects as go

from utils import (
    extract_text_from_pdf,
    generate_response,
    calculate_ats_score
)
from prompts import (
    RESUME_ANALYSIS_PROMPT,
    SKILLS_EXTRACTION_PROMPT,
    MISSING_SKILLS_PROMPT,
    INTERVIEW_QUESTIONS_PROMPT,
    COVER_LETTER_PROMPT,
    LINKEDIN_SUMMARY_PROMPT,
    ROADMAP_PROMPT
)

# Load environment variables from .env if present
load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer & Career Coach", layout="wide")

st.title("🚀 AI Resume Analyzer & Career Coach")
st.markdown("Upload your resume and provide a target job description to get AI-powered insights, ATS scoring, and career coaching!")

# Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    api_key_input = st.text_input("Groq API Key", type="password", help="Get your free API key at console.groq.com")
    if api_key_input:
        os.environ["GROQ_API_KEY"] = api_key_input
        
    st.markdown("---")
    st.markdown("### 👨‍💻 Developed by")
    st.markdown("**Khan Zaib**")
    st.markdown("[GitHub](https://github.com/khan-Zaib-00) | [LinkedIn](#)")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Upload Resume")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

with col2:
    st.subheader("Target Job Description")
    job_description = st.text_area("Paste the job description here (Required for ATS & Missing Skills)", height=150)

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    resume_text = extract_text_from_pdf(uploaded_file)
    
    st.success("Resume uploaded and processed successfully!")
    
    # Check if API Key is set
    # Try fetching from Streamlit secrets first if deployed
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
        
    if not os.environ.get("GROQ_API_KEY"):
        st.error("Please provide a Groq API Key in the sidebar, .env file, or Streamlit Secrets to continue.")
        st.stop()
        
    tabs = st.tabs([
        "📊 ATS Score & Skills", 
        "📝 Resume Analysis", 
        "❓ Interview Prep", 
        "📄 Cover Letter", 
        "🔗 LinkedIn Summary", 
        "🗺️ Roadmap"
    ])
    
    with tabs[0]:
        st.header("ATS Score & Skill Analysis")
        
        if job_description:
            with st.spinner("Calculating ATS Score..."):
                ats_score = calculate_ats_score(resume_text, job_description)
                
                # Plotly Gauge Chart for ATS Score
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = ats_score,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "ATS Compatibility Score"},
                    gauge = {
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 50], 'color': "red"},
                            {'range': [50, 80], 'color': "yellow"},
                            {'range': [80, 100], 'color': "green"}
                        ]
                    }
                ))
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Provide a Job Description to get your ATS Match Score.")
            
        col_skills, col_missing = st.columns(2)
        with col_skills:
            st.subheader("Identified Skills")
            if st.button("Extract Skills"):
                with st.spinner("Extracting skills..."):
                    skills = generate_response(SKILLS_EXTRACTION_PROMPT, resume_text=resume_text)
                    st.write(skills)
                    
        with col_missing:
            st.subheader("Missing Skills")
            if st.button("Find Missing Skills"):
                if job_description:
                    with st.spinner("Analyzing missing skills..."):
                        missing = generate_response(MISSING_SKILLS_PROMPT, resume_text=resume_text, job_description=job_description)
                        st.write(missing)
                else:
                    st.warning("Job Description is required for this feature.")
                    
    with tabs[1]:
        st.header("Resume Analysis & Improvement")
        if st.button("Analyze Resume"):
            with st.spinner("Analyzing..."):
                analysis = generate_response(RESUME_ANALYSIS_PROMPT, resume_text=resume_text, job_description=job_description or "Not provided")
                st.markdown(analysis)

    with tabs[2]:
        st.header("Interview Questions")
        if st.button("Generate Questions"):
            with st.spinner("Generating..."):
                questions = generate_response(INTERVIEW_QUESTIONS_PROMPT, resume_text=resume_text, job_description=job_description or "Not provided")
                st.markdown(questions)
                
    with tabs[3]:
        st.header("Cover Letter Generator")
        if st.button("Generate Cover Letter"):
            with st.spinner("Writing Cover Letter..."):
                cover_letter = generate_response(COVER_LETTER_PROMPT, resume_text=resume_text, job_description=job_description or "Not provided")
                st.markdown(cover_letter)
                
    with tabs[4]:
        st.header("LinkedIn Summary Generator")
        if st.button("Generate LinkedIn Summary"):
            with st.spinner("Writing LinkedIn Summary..."):
                linkedin = generate_response(LINKEDIN_SUMMARY_PROMPT, resume_text=resume_text)
                st.markdown(linkedin)

    with tabs[5]:
        st.header("Learning Roadmap")
        if st.button("Generate Roadmap"):
            with st.spinner("Creating Roadmap..."):
                roadmap = generate_response(ROADMAP_PROMPT, resume_text=resume_text, job_description=job_description or "Not provided")
                st.markdown(roadmap)
