import os 
import sys 
import requests

# Add path to the backend scripts 
dirname = os.path.dirname(
          os.path.dirname(
          os.path.abspath(__file__)
          ))
sys.path.append(dirname)

import streamlit as st
from backend.JobParser import JobParser
from backend.Analyzer import Analyzer
from backend.GlassdoorHelper import GlassdoorHelper
import matplotlib.pyplot as plt

st.title("Match Job Posting")

# Get passed linked url if any 
args = st.experimental_get_query_params()
linkedin_url = args.get("linkedin_url", [""])[0]

# Link input 
linkedin_url = st.text_input("LinkedIn Job Posting", value = linkedin_url)

try: 
    job_content = JobParser.__call__(linkedin_url)
except: 
    job_content = None

process_link = st.button("Process link") 

# Show resume analysis 
st.header("Posting Analysis")
resumes = requests.post("http://localhost:8000/resumes").json()

if process_link: 

    if job_content is not None:
        job_description = job_content.get_str()
        for i, r in enumerate(resumes):
            if r["file_name"] == "None": 
                resumes.pop(i)
        
        for r in resumes: 
            r["domain_score"] = Analyzer.get_domain_score(r["raw_text"], job_description)
            r["specialization_score"] = Analyzer.get_specialization_score(r["raw_text"], job_description)
            r["score"] = 2.*r["domain_score"] + 3.*r["specialization_score"]
            r["title"] = f'{r["file_name"]} ({r["score"]:.2f}/5.00)'
            r["skills"] = set(Analyzer.get_skills(r["raw_text"]))

        "#### Job Posting Keywords:"
        job_skills = set(Analyzer.get_skills(job_description))

        def display_skills(skills): 
            s = [f'<a style="border-radius: 10px; background: beige; padding: 5px; display: inline-block; margin-bottom: 0.75rem; margin-right: 0.75rem"> {k} </a>' for k in skills]
            st.markdown('<div style="font-color:white">' + "\n".join(s) + "</div>", unsafe_allow_html=True)

        display_skills(job_skills)

        if len(resumes) > 0: 
            tabs = st.tabs([r["title"] for r in resumes])

            for i, tab in enumerate(tabs): 
                with tab: 
                    "#### Resume Keywords:"
                    display_skills(resumes[i]["skills"])
                    " "
                    f'##### Domain Score:     {(100.*resumes[i]["domain_score"]):.2f} %'
                    st.progress(resumes[i]["domain_score"])

                    " "
                    f'##### Specialization Score:     {(100.*resumes[i]["specialization_score"]):.2f} %'
                    st.progress(resumes[i]["specialization_score"])

        helper = GlassdoorHelper()
        try: 
            glassdoorcontent = helper(helper, job_content, 2)
        except: 
            glassdoorcontent = None

        if glassdoorcontent is not None: 
            "### Glassdoor Reviews"
            st.write(glassdoorcontent.str_rep)


    else: 
        st.error("Could not process posting")