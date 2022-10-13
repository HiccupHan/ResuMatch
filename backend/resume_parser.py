"""
Look into:
    https://github.com/Spidy20/Smart_Resume_Analyser_App
    https://omkarpathak.in/pyresparser/
    https://pypi.org/project/pdfminer/
"""

from dataclasses import dataclass, field


@dataclass
class ResumeContent:
    """ Dataclass to collect and format parsed resume data """
    qual: list[str] = field(default_factory=list)
    exper: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    misc: list[str] = field(default_factory=list)
    user_id: str = ""


class ResumeParser:
    def __init__(self):
        pass

    @staticmethod
    def __call__(file_path : str) -> ResumeContent:
        """ Take in a file path to a pdf containing the resume and produce the needed ResumeContent"""
        raise NotImplementedError


