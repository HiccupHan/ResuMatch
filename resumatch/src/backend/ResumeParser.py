"""
Resume document parsing
"""

from dataclasses import dataclass, field

import spacy
from spacypdfreader import pdf_reader

@dataclass
class ResumeContent:
    """ Dataclass to collect and format parsed resume data """
    
    qual: list[str] = field(default_factory=list)
    """ Education and Qualifications """
    exper: list[str] = field(default_factory=list)
    """ Professional Experience """
    skills: list[str] = field(default_factory=list)
    """ Skills """
    misc: list[str] = field(default_factory=list)
    """ Miscellaneous """
    user_id: str = ""
    """ Unique User ID """


class ResumeParser:
    """ Parse Resume PDFs into usable format for analysis """
    _nlp = spacy.load('en_core_web_sm')

    def __init__(self):
        pass

    @staticmethod
    def get_raw_text(file_path: str): 
        '''
        takes a file path to resume pdf and returns the raw text 
        
        Parameters
        ----------
        file_path : str
            The path to the resume pdf file.
        
        Returns
        -------
            A string of the text from the resume.
        
        '''
        doc = pdf_reader(file_path, ResumeParser._nlp)
        return doc.text
