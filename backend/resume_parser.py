"""

"""

from dataclasses import dataclass


@dataclass
class ResumeContent:
    """ Dataclass to collect and format parsed resume data """
    qual: list[str] = []
    exper: list[str] = []
    skills: list[str] = []
    misc: list[str] = []
    user_id: str = ""


class ResumeParser:
    def __init__(self):
        pass

    @staticmethod
    def __call__(file_path : str) -> ResumeContent:
        """ Take in a file path to a pdf containing the resume and produce the needed ResumeContent"""
        raise NotImplementedError


