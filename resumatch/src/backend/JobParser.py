
"""
LinkedIn Job Posting Parsing
Resources:
    - https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/overview
"""
from dataclasses import dataclass, field

@dataclass
class JobContent:
    """ Dataclass to collect and format parsed LinkedIn Job Description data
    - *linkedin_url*: url to linked job posting
    - *company*: Company name
    - *job_title*: Job Title
    - *qual*: Required education and professional qualifications
    - *desc*: Job Description
    - *skills*: Required Skills
    - *misc*: Miscellaneous
    """

    linkedin_url: str = ""
    company: str = ""
    job_title: str = ""
    qual: list[str] = field(default_factory=list)
    desc: list[str] = field(default_factory=list)       #: job description
    skills: list[str] = field(default_factory=list)     #: required skills
    misc: list[str] = field(default_factory=list)       #: miscellaneous


class _BuildJobContent:
    """ Class to build job content dataclass based on web source """

    url: str
    source: str
    
    def __init__(self, url: str, source: str):
        self.url = url
        self.source = source
    
    def __call__(self) -> JobContent:
        job_content = JobContent(
            self.url, self.getCompany(), self.getJobTitle(), 
            self.getQual(), self.getDesc(), self.getSkills(), self.getMisc()
        )
        return job_content
        
    def getCompany(self):
        return ""
    
    def getJobTitle(self):
        return ""
    
    def getQual(self):
        return []
    
    def getDesc(self):
        return []
    
    def getSkills(self):
        return []
    
    def getMisc(self):
        return []

class JobParser:
    """ Class that returns job content of given url when called """
    def __init__(self):
        pass

    @staticmethod
    def run(linkedin_url : str) -> JobContent:
        """ Take in url to LinkedIn posting and produce the needed JobContent """
        source = JobParser.getSource(linkedin_url)               # get source code of url website
        builder = _BuildJobContent(linkedin_url, source)     # create builder for job content
        return builder()
    
    @staticmethod
    def getSource(linkedin_url):
        return ""