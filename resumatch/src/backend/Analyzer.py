"""
Resume analysis against a job description
Resources:
    - https://github.com/Spidy20/Smart_Resume_Analyser_App
    - https://deepnote.com/@abid/spaCy-Resume-Analysis-81ba1e4b-7fa8-45fe-ac7a-0b7bf3da7826
"""

from dataclasses import dataclass
# from .JobParser import JobContent
# from .ResumeParser import ResumeContent

import spacy
import numpy as np 
import os


class Analyzer:
    nlp = spacy.load("en_core_web_lg")
    skill_pattern_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jz_skill_patterns.jsonl")
    
    ruler = nlp.add_pipe("entity_ruler")
    ruler.from_disk(skill_pattern_path)

    """ Analyze job description against resume to give score """
    def __init__(self):
        pass

    @staticmethod
    def run_nlp(raw_text): 
        return Analyzer.nlp(raw_text)

    @staticmethod
    def get_skills(raw_text):
        doc = Analyzer.nlp(raw_text)
        skills = []

        for ent in doc.ents:
            if ent.label_ == "SKILL" or ent.label_ == "PRODUCT":
                skills.append(ent.text)

        return skills

    @staticmethod
    def get_score(resume_raw_text, job_desc_raw_text): 
        # Lower both and run through ner pipeline
        res_base = Analyzer.nlp(resume_raw_text.lower())
        job_base = Analyzer.nlp(job_desc_raw_text.lower())

        # Basic document similarity 
        sim_base = res_base.similarity(job_base)

        # Skill wise comparison 
        res_skills = [s.lower() for s in Analyzer.get_skills(resume_raw_text.lower())]
        res_skills.sort()

        job_skills = [s.lower() for s in Analyzer.get_skills(job_desc_raw_text.lower())]
        job_skills.sort()

        # Collect frequency of each skill
        skills = set()
        job_freq = {}
        res_freq = {}

        unique_skill, count = np.unique(job_skills, return_counts=True)
        for s, c in zip(unique_skill, count): 
            job_freq[s] = c 
            skills.add(s)

        unique_skill, count = np.unique(res_skills, return_counts=True)
        for s, c in zip(unique_skill, count): 
            res_freq[s] = c 
            skills.add(s)

        # Arrange in vectors 
        job_vec = np.zeros((len(skills), ))
        res_vec = np.zeros((len(skills), ))

        for i, s in enumerate(skills): 
            job_vec[i] = job_freq.get(s, 0.)
            res_vec[i] = res_freq.get(s, 0.)

        # Skill similarity 
        sim_skill = np.dot(job_vec, res_vec) / (np.linalg.norm(job_vec) * np.linalg.norm(res_vec))

        return 3.*sim_skill + 2.*sim_base