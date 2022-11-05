"""
Resume analysis against a job description

Resources:

    - https://github.com/Spidy20/Smart_Resume_Analyser_App
    - https://deepnote.com/@abid/spaCy-Resume-Analysis-81ba1e4b-7fa8-45fe-ac7a-0b7bf3da7826
"""

from dataclasses import dataclass
from .JobParser import JobContent
from .ResumeParser import ResumeContent


class Analyzer:
    """ Analyze job description against resume to give score """
    def __init__(self):
        pass

    @staticmethod
    def resume_score(job_content: JobContent, resume_content: ResumeContent) -> float:
        """ Take in job and resume content and give match score"""
        raise NotImplementedError

