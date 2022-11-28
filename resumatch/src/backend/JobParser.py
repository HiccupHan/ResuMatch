
"""
LinkedIn Job Posting Parsing
"""
import os
import sys
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
    
    def print(self, ofile=sys.stdout):
        print("--- Job Content ---", file=ofile)
        print("-- Company:", self.company, file=ofile)
        print("-- Job title:", self.job_title, file=ofile)
        
        print("-- Job description:", file=ofile)
        for idx in range(len(self.desc)):
            print("-", self.desc[idx], file=ofile)
        
        print("--- End of Job Content ---", file=ofile)

    def get_str(self):
        rstr = """"""
        rstr += self.company + "\n"
        rstr += self.job_title + "\n"
        for d in self.desc: 
            rstr += d + "\n"

        return rstr

class JobParser:
    """ Class that returns job content of given url when called """
    def __init__(self):
        pass

    @staticmethod
    def __call__(linkedin_url : str, fout_name : str = None) -> JobContent:
        """ Take in url to LinkedIn posting and produce the needed JobContent """
        
        source_text = getSource(linkedin_url, fout_name)
        builder = BuildJobContent(linkedin_url, source_text)
        
        return builder()

class BuildJobContent:
    """ Class to build job content dataclass based on web source """
    url : str
    soup : BeautifulSoup
    
    def __init__(self, url: str, source: str):
        self.url = url
        self.soup = BeautifulSoup(source, "lxml")
    
    def __call__(self) -> JobContent:
        try:
            job_content = JobContent(
                self.url, self.__getCompany(), self.__getJobTitle(), 
                self.__getQual(), self.__getDesc(), self.__getSkills(), self.__getMisc()
            )
            return job_content
        except:
            raise NotImplementedError
        
    def __getCompany(self) -> str:
        try: 
            key_line = self.soup.find('a', {'class' : 'sub-nav-cta__optional-url'})
            return key_line['title']
        except:
            print("Site content error: didn't find company name. ")
            raise NotImplementedError
    
    def __getJobTitle(self) -> str:
        try:
            key_line = self.soup.find('h3', {'class' : 'sub-nav-cta__header'})
            return key_line.contents[0]
        except:
            print("Site content error: didn't find job title. ")
            raise NotImplementedError
    
    def __getQual(self) -> str:
        return None
    
    def __getDesc(self) -> str:
        try: 
            key_line = self.soup.find('div', \
                {'class' : 'show-more-less-html__markup show-more-less-html__markup--clamp-after-5'})
            contents = key_line.contents
        except:
            print("Site content error: didn't find job descriptions. ")
            raise NotImplementedError
        
        new_contents = []
        for line in contents:
            line = str(line)
            langles = findIndexes(line, '<')
            rangles = findIndexes(line, '>')
            num_ang = len(langles)
            
            new_str = ''
            if num_ang > 0:
                for _ in range(num_ang):
                    new_str += line[0 if _ == 0 else rangles[_ - 1] + 1 : langles[_]]
                new_str += line[rangles[num_ang - 1] + 1 :]
            else:
                new_str = line
                
            if len(new_str) > 0:
                new_contents.append(new_str)
        
        return new_contents
    
    def __getSkills(self) -> str:
        return None
    
    def __getMisc(self) -> str:
        return None

def findIndexes(s : str, c : str):
    """ Returns the list of indexes i where s[i] = c """
    assert len(c) == 1
    return [i for i, ltr in enumerate(s) if ltr == c]

def remakeFile(file_name):
    if os.path.exists(file_name): 
        os.system('rm -r ' + file_name)
    try: 
        os.system('touch ' + file_name)
    except:
        print('Unable to create file: ', file_name + ' . ')
        raise NotImplementedError
    
def getSource(url, file_name=None) -> str:
    """ 
        Get source code of given url. 
        If file_name is provided, also print to file. 
    """
    try: 
        text = requests.get(url).text
    except:
        print('Unable to open URL ' + \
            (url if len(url) <= 50 else url[:50]+'...') + ' . ')
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
