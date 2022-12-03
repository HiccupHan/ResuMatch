'''
Resume analysis against a job description

Resources:

- https://github.com/Spidy20/Smart_Resume_Analyser_App

- https://deepnote.com/@abid/spaCy-Resume-Analysis-81ba1e4b-7fa8-45fe-ac7a-0b7bf3da7826
'''

from dataclasses import dataclass

import spacy
import numpy as np 
import os


class Analyzer:
    ''' Process resume and job description text though NLP Analysis and generate matching score '''
    
    # Loading the English language NLP model
    _nlp = spacy.load("en_core_web_lg")

    # Loading the skill pattern data for NER analysis 
    _skill_pattern_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jz_skill_patterns.jsonl")
    
    # Loading NER model to NLP pipeline
    _ruler = _nlp.add_pipe("entity_ruler")
    _ruler.from_disk(_skill_pattern_path)

    def __init__(self):
        pass

    @staticmethod
    def run_nlp(raw_text: str): 
        '''
        Takes in a string of text, and returns a list of dictionaries, where each
        dictionary contains the information about a single sentence
        
        Parameters
        ----------
        raw_text : str
            The text to be analyzed.
        
        Returns
        -------
            A list of dictionaries containing the text, lemma, pos, and tag of each word in the text
        
        '''
        return Analyzer._nlp(raw_text)

    @staticmethod
    def get_skills(raw_text: str) -> list[str]:
        '''
        Takes a string of text, and returns a list of skills through NER analysis
        
        Parameters
        ----------
        raw_text : str
            The text to be analyzed.
        
        Returns
        -------
        list[str]
            A list of skills
        
        '''

        doc = Analyzer._nlp(raw_text)
        skills = []

        for ent in doc.ents:
            if ent.label_ == "SKILL" or ent.label_ == "PRODUCT":
                skills.append(ent.text)

        skills = [s.lower() for s in skills]
        skills.sort()

        return skills

    @staticmethod
    def get_domain_score(resume_raw_text: str, job_desc_raw_text: str) -> float: 
        '''
        Take the raw text of the resume and job description and compare them
        
        The similarity score is a measure of how similar two documents are. 
        It's a number between 0 and 1, where 1 is the most similar. 
        
        Parameters
        ----------
        resume_raw_text : str
            The raw text of the resume
        job_desc_raw_text : str
            The raw text of the job description
        
        Returns
        -------
        float
            A similarity score between 0 and 1.
        
        '''

        # Lower both and run through ner pipeline
        res_base = Analyzer._nlp(resume_raw_text.lower())
        job_base = Analyzer._nlp(job_desc_raw_text.lower())

        # Basic document similarity 
        sim_base = res_base.similarity(job_base)

        return sim_base

    @staticmethod
    def get_specialization_score(resume_raw_text: str, job_desc_raw_text: str) -> float: 
        '''
        Take the skills from the resume and job description and compare the frequencies
        
        The similarity score is a measure of how similar two documents are. 
        It's a number between 0 and 1, where 1 is the most similar. 
        
        Parameters
        ----------
        resume_raw_text : str
            The raw text of the resume.
        job_desc_raw_text : str
            The raw text of the job description.

        Returns
        -------
        float
            A similarity score between 0 and 1.
        
        '''
        # Skill wise comparison 
        res_skills = Analyzer.get_skills(resume_raw_text.lower())
        job_skills = Analyzer.get_skills(job_desc_raw_text.lower())

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

        return sim_skill

    @staticmethod
    def get_score(resume_raw_text: str, job_desc_raw_text: str) -> float: 
        '''
        Take resume and a job description, and return a similarity score between 0 and 5
        
        Parameters
        ----------
        resume_raw_text : str
            The raw text of the resume
        job_desc_raw_text : str
            The raw text of the job description
        
        Returns
        -------
        float
            A similarity score between 0 and 5.
        
        '''

        sim_base  = Analyzer.get_domain_score(resume_raw_text, job_desc_raw_text)
        sim_skill = Analyzer.get_specialization_score(resume_raw_text, job_desc_raw_text)

        return 3.*sim_skill + 2.*sim_base