"""
Look into:
    https://github.com/Spidy20/Smart_Resume_Analyser_App
    https://deepnote.com/@abid/spaCy-Resume-Analysis-81ba1e4b-7fa8-45fe-ac7a-0b7bf3da7826
"""

from dataclasses import dataclass
from .job_parser import JobContent
from .resume_parser import ResumeContent


class Analyzer:
    def __init__(self):
        pass

    @staticmethod
    def resume_score(job_content: JobContent, resume_content: ResumeContent) -> tuple[JobContent, ResumeContent, float]:
        """ Take in job and resume content and give match score"""
        raise NotImplementedError

    def qual_match(job_qual: list, resume_qual: list) -> tuple[list, float]:
        """ Match qualifications. """

    def exper_match(job_desc: list, resum_exper: list) -> tuple[list, float]:
        """ Match job description with user's working experience """

    def skills_match(job_skills: list, resume_skills: list) -> tuple[list, float]:
        """Match job's required skills and user's skills"""

    def type_match(job_misc: list, resume_misc: list) -> tuple[list, float]:
        """ Match job type: internship/part-time/full-time. If internship, further match  duration. If part-time, further match working hours. The tuple should include work type, duration, working hours, etc."""

    def misc_match(job_misc: list, resume_misc: list) -> tuple[list, float]:
        """ Match other things """

