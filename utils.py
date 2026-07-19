import os
import PyPDF2
from langchain_groq import ChatGroq
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

def get_llm():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    # Using Llama 3 for fast and reliable generation
    return ChatGroq(groq_api_key=api_key, model_name="llama-3.3-70b-versatile")

def generate_response(prompt_template, **kwargs):
    llm = get_llm()
    chain = prompt_template | llm
    response = chain.invoke(kwargs)
    return response.content

def calculate_ats_score(resume_text, job_description):
    if not job_description.strip():
        return 0.0
    
    # Load sentence transformer model to generate embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for both texts
    embeddings = model.encode([resume_text, job_description])
    
    # Calculate cosine similarity
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    # Convert to percentage and return
    return round(float(score) * 100, 2)
