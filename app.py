import streamlit as st
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page Configuration
st.set_page_config(
    page_title="CareerPath AI",
    page_icon="🎯",
    layout="centered"
)

st.title("CareerPath AI: Agentic Career Guidance & Resume Builder")
st.write(
    "Analyze your skills against industry requirements and receive an automated, "
    "AI-generated upskilling roadmap."
)

# User Input Form
with st.form("career_form"):
    full_name = st.text_input("Full Name", placeholder="e.g., Abdul Sattar")
    user_email = st.text_input(
        "Email Address (For AI Roadmap Delivery)",
        placeholder="e.g., a.sattar786basheer@gmail.com"
    )
    user_skills = st.text_area(
        "Your Current Skills (e.g., Python, SQL, Communication)",
        placeholder="Python, SQL, Machine Learning, HTML, CSS"
    )
    target_role = st.text_input(
        "Target Job Role (e.g., Data Analyst)",
        placeholder="Data Analyst"
    )
    job_description = st.text_area(
        "Job Description / Required Skills",
        placeholder="Requires Python, SQL, Data Analysis, and good communication skills."
    )
    
    # Optional Zapier Webhook URL for live automation
    zapier_webhook = st.text_input(
        "Zapier Webhook URL (Optional - leave blank for demo mode)",
        type="password"
    )
    
    submitted = st.form_submit_button("Analyze & Trigger AI Agent")

if submitted:
    if not user_skills.strip() or not job_description.strip():
        st.error("Please enter both your current skills and the target job description.")
    else:
        # Compute TF-IDF & Cosine Similarity
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform([user_skills, job_description])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_score = round(similarity * 100, 1)

        st.subheader(f"Skill Match Score: {match_score}%")
        st.progress(min(int(match_score), 100))

        if match_score >= 70:
            st.success("Strong alignment! Your profile matches the core job requirements.")
        else:
            st.warning("You have skill gaps. Upskilling is recommended.")

        # Trigger Agentic AI Pipeline (Zapier -> Gemini LLM -> Gmail)
        payload = {
            "name": full_name,
            "email": user_email,
            "skills": user_skills,
            "target_role": target_role,
            "job_description": job_description,
            "match_score": match_score
        }

        if zapier_webhook.strip():
            try:
                response = requests.post(zapier_webhook.strip(), json=payload, timeout=10)
                if response.status_code == 200:
                    st.info(f"Agentic Workflow Triggered! Personalized roadmap dispatched to {user_email}.")
                else:
                    st.warning("Score calculated, but webhook returned a non-200 status.")
            except Exception as e:
                st.error(f"Webhook connection error: {e}")
        else:
            st.info(
                f"Agentic AI Triggered: Generating 3-step upskilling roadmap for "
                f"**{target_role or 'Target Role'}** and queuing delivery to **{user_email or 'user email'}**."
            )
