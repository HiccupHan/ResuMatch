"""
Look into:
    https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/overview
"""

from dataclasses import dataclass, field


@dataclass
class JobContent:
    """ Dataclass to collect and format parsed LinkedIn Job Description data """
    qual: list[str] = field(default_factory=list)
    desc: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    misc: list[str] = field(default_factory=list)
    company: str = ""
    linkedin_url: str = ""


class JobParser:
    def __init__(self):
        pass

    @staticmethod
    def __call__(linkedin_url : str) -> JobContent:
        """ Take in url to LinkedIn posting and produce the needed JobContent"""
        raise NotImplementedError


