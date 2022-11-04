"""
Look into:
    https://github.com/Spidy20/Smart_Resume_Analyser_App
    https://omkarpathak.in/pyresparser/
    https://pypi.org/project/pdfminer/
"""

from dataclasses import dataclass, field
from pyresparser import ResumeParser

@dataclass
class ResumeContent:
    """ Dataclass to collect and format parsed resume data """
    qual: list[str] = field(default_factory=list)
    exper: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    misc: list[str] = field(default_factory=list)
    user_id: str = ""


class ResumeContentAdapter:
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


class myResumeParser:
    """My own ResumeParser"""

    def __init__(self):
        pass

    @staticmethod
    def __call__(file_path: str) -> ResumeContent:
        rp = ResumeParser(file_path).get_extracted_data()
        return ResumeContentAdapter.produceResumeContent(rp)
        """ Take in a file path to a pdf containing the resume and produce the needed ResumeContent"""
        raise NotImplementedError


