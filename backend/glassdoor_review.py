"""
Look into:
    https://www.glassdoor.com/developer/index.htm
"""

from dataclasses import dataclass, field


@dataclass
class GlassdoorContent:
    """ Dataclass to collect and format parsed glassdoor data """
    rating: float = -1.
    reviews: list[str] = field(default_factory=list)
    linkedin_url: str = ""
    glassdoor_url: str = ""


class GlassdoorHelper:
    def __init__(self):
        pass

    @staticmethod
    def __call__(linkedin_url : str) -> GlassdoorContent:
        """ Take in url to linkedin and produce the needed GlassdoorContent"""
        raise NotImplementedError


