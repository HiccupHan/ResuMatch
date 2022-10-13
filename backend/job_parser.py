"""
Look into:
    https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/overview
"""

from dataclasses import dataclass


@dataclass
class JobContent:
    """ Dataclass to collect and format parsed LinkedIn Job Description data """
    qual: list[str] = []
    desc: list[str] = []
    skills: list[str] = []
    misc: list[str] = []
    company: str = ""
    linkedin_url: str = ""


class JobParser:
    def __init__(self):
        pass

    @staticmethod
    def __call__(linkedin_url : str) -> JobContent:
        """ Take in url to LinkedIn posting and produce the needed JobContent"""
        raise NotImplementedError


