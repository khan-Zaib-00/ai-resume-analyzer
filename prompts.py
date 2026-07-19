from langchain_core.prompts import PromptTemplate

RESUME_ANALYSIS_PROMPT = PromptTemplate.from_template("""
You are an expert HR professional and Career Coach. Please analyze the following resume and provide constructive feedback.
If a Job Description is provided, tailor your feedback to how well the resume matches the job.

Job Description: {job_description}

Resume Text:
{resume_text}

Provide your analysis covering:
1. **Overall Strengths**: What stands out in the resume.
2. **Areas for Improvement**: Formatting, impact, missing action verbs, etc.
3. **Summary**: A brief executive summary of the candidate's profile.
""")

SKILLS_EXTRACTION_PROMPT = PromptTemplate.from_template("""
Extract a clean, comma-separated list of all technical and soft skills present in the following resume.
Do not include any extra text.

Resume Text:
{resume_text}

Skills:
""")

MISSING_SKILLS_PROMPT = PromptTemplate.from_template("""
Given the following Job Description and the Candidate's Resume, identify the key skills required by the job that are missing from the resume.

Job Description: {job_description}

Resume Text:
{resume_text}

Provide a clear list of the missing skills. If no job description is provided, say "Please provide a Job Description to identify missing skills."
""")

INTERVIEW_QUESTIONS_PROMPT = PromptTemplate.from_template("""
Based on the following resume and the target job description (if provided), generate 5 challenging and relevant interview questions for this candidate.
For each question, provide a brief tip on how the candidate should answer it.

Job Description: {job_description}

Resume Text:
{resume_text}
""")

COVER_LETTER_PROMPT = PromptTemplate.from_template("""
Write a professional, compelling, and concise cover letter for the candidate based on their resume and the target job description.

Job Description: {job_description}

Resume Text:
{resume_text}
""")

LINKEDIN_SUMMARY_PROMPT = PromptTemplate.from_template("""
Based on the following resume, write an engaging and professional LinkedIn "About" section summary for the candidate.
Keep it between 3 to 4 paragraphs, highlighting their top achievements, skills, and career trajectory.

Resume Text:
{resume_text}
""")

ROADMAP_PROMPT = PromptTemplate.from_template("""
Based on the candidate's resume and their target job description, generate a step-by-step learning roadmap to help them acquire the missing skills and become a highly competitive candidate.

Job Description: {job_description}

Resume Text:
{resume_text}

Provide the roadmap in a clear, structured markdown format.
""")
