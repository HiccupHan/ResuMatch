"""
Glassdoor reviews
Resources:
    - https://www.glassdoor.com/developer/index.htm
"""

from dataclasses import dataclass, field


@dataclass
class GlassdoorContent:
    """ Dataclass to collect and format parsed glassdoor data
    - *rating*: Glassdoor company ratings
    - *reviews*: Selected comapny reviews from glassdoor
    - *linkedin_url*: LinkedIn posting url
    - *glassdoor_url*: Glassdoor reviews url
    """
    rating: float = -1.
    reviews: list[str] = field(default_factory=list)
    linkedin_url: str = ""
    glassdoor_url: str = ""


class GlassdoorHelper:
    """ Obtain needed information from glassdoor about LinkedIn posting """
    def __init__(self):
        pass

    @staticmethod
    def run(linkedin_url : str) -> GlassdoorContent:
        """ Take in url to linkedin and produce the needed GlassdoorContent"""
        raise NotImplementedError