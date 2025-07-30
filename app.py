import streamlit as st
import os
from resume_parser import extract_text
from summarizer import summarize_text
from matcher import match_summary_to_job
from utils import save_results

st.title("🧠 Resume Matcher App")

uploaded_files = st.file_uploader("Upload multiple resumes (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

job_description = st.text_area("Paste job description here", height=200)

if st.button("Run Resume Matching") and uploaded_files:
    for uploaded_file in uploaded_files:
        # resume_text = extract_text(uploaded_file.name)
        resume_text = extract_text(uploaded_file)

        summary = summarize_text(resume_text)
        match_status, score = match_summary_to_job(summary, job_description)
        save_results(summary, match_status, score, uploaded_file.name.split('.')[0])

        st.write(f"📄 **{uploaded_file.name}**")
        st.write(f"✔️ Match Status: {match_status}")
        st.write(f"📊 Match Score: {score}")
        st.write(f"📝 Summary: {summary[:250]}...")

    st.success("🎉 Matching completed! Check output folder for results.")
