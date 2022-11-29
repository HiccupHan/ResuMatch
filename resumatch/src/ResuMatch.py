import streamlit as st
import os
import requests
import spacy_streamlit
import re

from backend.Analyzer import Analyzer

def upload_page(): 
    
    st.title('ResuMatch')

    st.text("Welcome! Please upload a resume or select one that has already been uploaded")

    resume_names = requests.post("http://localhost:8000/resume_names").json()
    if "resume_names" not in st.session_state: 
        st.session_state["resume_names"] = resume_names

    st.subheader("Upload Resume")
    resume_file = st.file_uploader("Resume", type="pdf")

    if st.button("Process file") and resume_file is not None: 
        file_name = resume_file.name
        fpath = os.path.join("src/backend/.resumatch", file_name)

        with open(fpath, 'wb') as f: 
            f.write(resume_file.getvalue())

        fpath = os.path.join(".resumatch", file_name)
        requests.post(f"http://localhost:8000/add_resume?resume_file_path={fpath}")
        st.session_state["resume_names"] = requests.post("http://localhost:8000/resume_names").json()

    st.subheader("Select Resume")
    selection = st.selectbox("Uploaded Resumes", st.session_state["resume_names"])
    print(st.session_state["resume_names"])

    if selection != "None": 
        resumes = requests.post("http://localhost:8000/resumes").json()
        for r in resumes: 
            if r["file_name"] == selection: 
                raw_text = r["raw_text"].split("\n")
                cleaned_lines = []

                for i, s in enumerate(raw_text): 
                    s = re.sub(r'\s+', " ", s)
                    if(len(s) > 0 and s != " "): 
                        cleaned_lines.append(s)
                
                raw_text = '\n'.join(cleaned_lines)
                spacy_streamlit.visualize_ner(Analyzer.nlp(raw_text))

upload_page()