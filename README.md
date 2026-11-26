# CareerPath AI: Agentic Career Guidance & Resume Skill-Gap Analyzer

An autonomous Machine Learning and Agentic AI career guidance system built under the **IBM SkillsBuild – AICTE – BharatCares (CSRBOX) Applied AI Internship 2026**, aligned with **UN Sustainable Development Goal 8 (Decent Work and Economic Growth)**.

## Overview
Many graduates and job seekers in Tier-2 and Tier-3 cities apply for roles without knowing the exact technical skills missing from their profiles. **CareerPath AI** evaluates candidate skills against target job descriptions using Natural Language Processing (NLP) and triggers an autonomous AI workflow to email a customized 3-step upskilling roadmap directly to the user.

## System Architecture (`Perceive → Reason → Act`)
1. **Perceive (Streamlit Web Interface):** Collects the candidate's current skills, target job role, job description, and email address.
2. **ML Scoring (Scikit-learn NLP):** Uses `TfidfVectorizer` and `cosine_similarity` to compute a quantitative Skill Match Score (validated at **24.4%** on a sample Data Analyst profile).
3. **Reason (Zapier + Google Gemini):** Triggers a multi-step Zapier pipeline (`Google Sheets → Google AI Studio Gemini`) to generate a tailored 3-step study roadmap based on identified skill gaps.
4. **Act (Automated Gmail Delivery):** Dispatches the personalized upskilling plan directly to the candidate's inbox without manual intervention.

## Tech Stack
* **Frontend & UI:** Python, Streamlit
* **Machine Learning & NLP:** Scikit-learn (`TfidfVectorizer`, `cosine_similarity`)
* **Agentic Automation:** Zapier, Google AI Studio (Gemini LLM), Gmail Integration

## Project Deliverables & Documentation
* [Concept Note & Lean Canvas (PDF)](./docs/CareerPath%20AI%20-%20Concept%20Note%20&%20Lean%20Canvas.pdf)
* [Final Deliverable Presentation (PPTX)](./docs/CareerPath%20AI%20-%20Final%20Deliverable%20Presentation.pptx)
* [Prototype & Workflow Execution Screenshots (PDF)](./docs/Project_Screenshots.pdf)

## Run Locally
```bash
git clone [https://github.com/](https://github.com/)<your-github-username>/CareerPath-AI.git
cd CareerPath-AI
pip install -r requirements.txt
streamlit run app.py
