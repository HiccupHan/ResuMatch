"""
Resume document parsing
Resources:
    - https://github.com/Spidy20/Smart_Resume_Analyser_App
    - https://omkarpathak.in/pyresparser/
    - https://pypi.org/project/pdfminer/
"""

from dataclasses import dataclass, field
# from pyresparser import ResumeParser as rparser

import spacy
from spacypdfreader import pdf_reader

@dataclass
class ResumeContent:
    """ Dataclass to collect and format parsed resume data
    - *qual*: Education and Qualifications
    - *exper*: Professional Experience
    - *skills*: Skills
    - *misc*: Miscellaneous
    - *user_id*: Unique User ID
    """
    qual: list[str] = field(default_factory=list)
    exper: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    misc: list[str] = field(default_factory=list)
    user_id: str = ""


class _ResumeContentAdapter:
    """class to transform the data from API to ResumeContent """

    def __init__(self):
        pass

    def produceResumeContent(self, data):
        resume_content = ResumeContent()
        resume_content.qual = data[0]["designation"]
        resume_content.exper = data[0]['total_experience']
        resume_content.skills = data[0]['skills']
        resume_content.misc = data[0]
        resume_content.user_id = data[0]['name']
        return resume_content


class ResumeParser:
    """ Parse Resume PDFs into usable format for analysis """
    nlp = spacy.load('en_core_web_sm')

    def __init__(self):
        pass

    @staticmethod
    def get_raw_text(file_path: str): 
        doc = pdf_reader(file_path, ResumeParser.nlp)
        return doc.text

    # @staticmethod
    # def run(file_path: str) -> ResumeContent:
    #     """ Take in a file path to a pdf containing the resume and produce the needed ResumeContent"""
    #     rp = rparser(file_path).get_extracted_data()
    #     return _ResumeContentAdapter().produceResumeContent(rp)