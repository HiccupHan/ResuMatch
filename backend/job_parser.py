import os
import requests
from dataclasses import dataclass, field
from typing import List
from bs4 import BeautifulSoup

@dataclass
class JobContent:
    """ Dataclass to collect and format parsed LinkedIn Job Description data """
    linkedin_url: str = ""
    company: str = ""
    job_title: str = ""
    qual: List[str] = field(default_factory=list)       # qualifications
    desc: List[str] = field(default_factory=list)       # job description
    skills: List[str] = field(default_factory=list)     # required skills
    misc: List[str] = field(default_factory=list)       # miscellaneous

class JobParser:
    """ Class that returns job content of given url when called """
    def __init__(self):
        pass

    @staticmethod
    def __call__(linkedin_url : str) -> JobContent:
        """ Take in url to LinkedIn posting and produce the needed JobContent """
        
        fout_name = 'page_source.txt'
        try:
            source_text = getSource(linkedin_url, fout_name)
        except:
            print('Unable to acquire source. ')
            raise NotImplementedError
        
        builder = BuildJobContent(linkedin_url, source_text)
        
        try: 
            job_content = builder()
            return job_content
        except:
            raise NotImplementedError

class BuildJobContent:
    """ Class to build job content dataclass based on web source """
    url : str
    soup : BeautifulSoup
    
    def __init__(self, url: str, source: str):
        self.url = url
        self.soup = BeautifulSoup(source, "lxml")
    
    def __call__(self) -> JobContent:
        job_content = JobContent(
            self.url, self.__getCompany(), self.__getJobTitle(), 
            self.__getQual(), self.__getDesc(), self.__getSkills(), self.__getMisc()
        )
        return job_content
        
    def __getCompany(self) -> str:
        key_line = self.soup.find('a', {'class' : 'sub-nav-cta__optional-url'})
        return key_line['title']
    
    def __getJobTitle(self) -> str:
        key_line = self.soup.find('h3', {'class' : 'sub-nav-cta__header'})
        return key_line.contents[0]
    
    def __getQual(self) -> str:
        return None
    
    def __getDesc(self) -> str:
        return None
    
    def __getSkills(self) -> str:
        return None
    
    def __getMisc(self) -> str:
        return None

def remakeFile(file_name):
    if os.path.exists(file_name): 
        os.system('rm -r ' + file_name)
    try: 
        os.system('touch ' + file_name)
    except:
        print('Unable to create file: ', file_name + ' . ')
        raise NotImplementedError
    
def getSource(linkedin_url, file_name=None) -> str:
    """ 
        Get source code of given url. 
        If file_name is provided, also print to file. 
    """
    try: 
        text = requests.get(linkedin_url).text
    except:
        print('Unable to open URL ' + \
            (linkedin_url if len(linkedin_url) <= 50 else linkedin_url[:50]+'...') + ' . ')
        raise NotImplementedError
    
    if file_name is not None: 
        try: 
            remakeFile(file_name)
        except:
            pass
        else:
            try: 
                with open(file_name, 'w') as fid:
                    fid.write(text)
            except: 
                print('Unable to open file ' + file_name + ' . ')
    
    return text

job_sites = [
    "https://www.linkedin.com/jobs/view/3344591035", # Activision, UI/UX Internship
    "https://www.linkedin.com/jobs/view/3362600474", # Google, Principal Architect
    "https://www.linkedin.com/jobs/view/3365151981", # CyberCoders, Web Developer
]

parser = JobParser()
for idx in range(len(job_sites)):
    print(parser(job_sites[idx]))
