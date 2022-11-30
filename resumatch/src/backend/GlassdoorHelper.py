"""
Look into:
    https://www.glassdoor.com/developer/index.htm
    https://stackoverflow.com/questions/58040225/enter-query-in-search-bar-and-scrape-results
"""

from dataclasses import dataclass, field
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as soup
from typing import List
from .JobParser import JobContent, JobParser

def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

@dataclass
class GlassdoorContent:
    """ Dataclass to collect and format parsed glassdoor data """
    flag: bool = False
    rating: float = -1.
    recommandation: str = "0%"
    approval: str = "0%"
    breif_reviews: list = field(default_factory=lambda : [])
    pros: list = field(default_factory=lambda : [])
    cons: list = field(default_factory=lambda : [])
    str_rep: str = ""
    glassdoor_url: str = "https://www.glassdoor.co.in/member/home/companies.htm"


class GlassdoorHelper:
    
    def __init__(self):
        self.company = None
        self.job_title = None
    
    
    @staticmethod
    def __call__(self, jobcontent : JobContent, flag: int) -> GlassdoorContent:
        """ Take in job title and company to produce the needed GlassdoorContent"""
        
        # search company
        str_rep = ""
        if flag==1:
            self.company = jobcontent.company
            links = scrape_google("glassdoor "+self.company)
            link = None
            for l in links:
                if l.startswith("https://www.glassdoor.com/Overview/"):
                    link=l
                    break
            print('The link is '+link)
            
            # set headers
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

            # set get request
            html = requests.get(link, headers = headers)
            bsobj = soup(html.content,'lxml')
            
            # scarpe rating
            rating=-1
            rating=bsobj.findAll('div',{'class':'mr-xsm css-1c86vvj eky1qiu0'})[0].text.strip()
            print('The rating of '+self.company+' is '+rating)
            
            # scarpe recommandation to a friend
            recommandation=-1
            recommandation=bsobj.findAll('text',{'class':'text css-xsmmgf'})[0].text.strip()
            print(recommandation+' of '+self.company+' employees will recommand this company to a friend')
            
            # scrape approve of CEO
            approval=-1
            approval=bsobj.findAll('text',{'class':'text css-xsmmgf'})[1].text.strip()
            print(approval+' of '+self.company+' employees approve of CEO')
            
            # scrape reviews
            links = scrape_google("glassdoor "+self.company+" reviews")
            link_ = None
            #print(links)
            links_ = []
            for l in links:
                if l.startswith("https://www.glassdoor.com/Reviews/"):
                    if "HR" not in l:
                        links_.append(l)
                        link_=l
            # print(links_)
            print('The link is '+link_)
            html = requests.get(link_, headers = headers)
            bsobj = soup(html.content,'lxml')
            review_obj=bsobj.findAll('h2',{'class':'mb-xxsm mt-0 css-93svrw el6ke055'})
            review_list=[i.text.strip() for i in review_obj]
            print('Brief Reviews:',review_list)
            
            # scrape pros and cons
            pros_and_cons_obj=bsobj.findAll('div',{'class':'v2__EIReviewDetailsV2__fullWidth'})
            pros_list=[]
            cons_list=[]
            pros_and_cons=[i.text.strip() for i in pros_and_cons_obj]
            for s in pros_and_cons:
                if s.startswith('Pro'):
                    pros_list.append(s[4:])
                elif s.startswith('Con'):
                    cons_list.append(s[4:])
            print('Pros:', pros_list)
            print('Cons:', cons_list)
            
            return GlassdoorContent(True,rating,recommandation,approval,review_list,pros_list,cons_list,link)
        
        # search company and job title
        elif flag==2:
            self.company = jobcontent.company
            self.job_title = jobcontent.job_title
            links = scrape_google("glassdoor rating"+self.company+" "+self.job_title)
            link = None
            for l in links:
                if l.startswith("https://www.glassdoor.com/Reviews/"):
                    link=l
                    break
            if link==None:
                print('There is no rating or reviews for '+self.company+" "+self.job_title+' on Glassdoor')
                str_rep += 'There is no rating or reviews for '+self.company+" "+self.job_title+' on Glassdoor' + "\n"
                return GlassdoorContent(str_rep=str_rep)
            else:
                print('The link is '+link)
            
            # set headers
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
            
            # set get request
            html = requests.get(link, headers = headers)
            bsobj = soup(html.content,'lxml')
            
            # scrape exact job title
            exact_job_title=bsobj.findAll('header',{'class':'row justify-content-between align-items-center mb-std'})[0].h1.text.strip()[:-8]
            
            # scarpe rating
            rating=-1
            rating=bsobj.findAll('div',{'class':'v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__large'})[0].text.strip()
            print('The rating of '+exact_job_title+' is '+rating)
            str_rep += 'The rating of '+exact_job_title+' is '+rating  + "\n"
            
            # scarpe recommandation
            recommandation=-1
            recommandation=bsobj.findAll('div',{'class':'donut__DonutStyleV2__donuttext donut-text pt-lg-0 px-lg-sm'})[0].findAll('strong')[0].text.strip()
            print(recommandation+' of '+exact_job_title+' employees will recommand this job to a friend')
            str_rep += recommandation+' of '+exact_job_title+' employees will recommand this job to a friend'  + "\n"

            # scarpe approval of CEO
            approval=-1
            approval_obj = bsobj.findAll('div',{'class':'donut__DonutStyleV2__donuttext donut-text pt-lg-0 px-lg-sm'})
            if len(approval_obj)>1:
                approval=bsobj.findAll('div',{'class':'donut__DonutStyleV2__donuttext donut-text pt-lg-0 px-lg-sm'})[1].findAll('strong')[0].text.strip()
                print(approval+' of '+exact_job_title+' employees approve of CEO')
                str_rep += approval+' of '+exact_job_title+' employees approve of CEO'  + "\n"
            
            # scrape reviews
            review_list=[i.text.strip() for i in bsobj.findAll('h2',{'class':'mb-xxsm mt-0 css-93svrw el6ke055'})]
            print('Brief Reviews:',review_list)
            str_rep += 'Brief Reviews: ' + str(review_list)  + "\n"

            # scrape pros
            pros_obj=bsobj.findAll('div',{'class':'v2__EIReviewDetailsV2__fullWidth'})[::2]
            pros_list=[i.text.strip()[4:] for i in pros_obj]
            print('Pros:',pros_list)
            str_rep += 'Pros: ' + str(pros_list)  + "\n"

            # scrape cons
            cons_obj=bsobj.findAll('div',{'class':'v2__EIReviewDetailsV2__fullWidth'})[1::2]
            cons_list=[i.text.strip()[4:] for i in cons_obj]
            print('Cons:',cons_list)
            str_rep += 'Cons: ' + str(cons_list)  + "\n"

            return GlassdoorContent(True,rating,recommandation,approval,review_list,pros_list,cons_list,link)

        else:
            raise TypeError('''The second argument should be 1 or 2: 
                            1 corresponds to searching company name on glassdoor, 
                            2 corresponds to searching company name and job title on glassdoor.''')
        
           
        # raise NotImplementedError

# linkedin_site = "https://www.linkedin.com/jobs/view/3344591035"
# helper = GlassdoorHelper()
# parser = JobParser()
# jobcontent = parser(linkedin_site)
# glassdoorcontent = helper(helper, jobcontent,2)
