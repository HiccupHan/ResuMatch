'''
FastAPI server module
'''

from fastapi import FastAPI
from .Database import *
from .Analyzer import Analyzer
from .JobParser import JobParser

# Store user data locally 
_user_data_dir = ".resumatch"

# Fast API App 
_app = FastAPI()

# Level DB local database 
db = get_data(_user_data_dir)

def get_db() -> plyvel.DB: 
    """ Get the database """
    if db.closed: 
        return get_data(_user_data_dir)
    return db

@_app.post("/resume_names")
def backend_get_resume_names() -> list[str]: 
    """ Get names of resumes stored in database """
    return get_resume_names(get_db())

@_app.post("/resumes")
def backend_get_data_json() -> list[dict]: 
    """ Get each resume's stored data """
    return get_data_json(get_db())["resumes"]

@_app.post("/add_resume")
def backend_add_resume(resume_file_path: str): 
    """ Load resume pdf from path, parse and add to database """
    return add_resume(get_db(), resume_file_path)

# Add a remove resume 
@_app.get("/remove_resume")
def backend_remove_resume(resume_file_name: str): 
    """ Remove resume with file name from database """
    return remove_resume(get_db(), resume_file_name)

@_app.get("/scores")
def backend_scores(linkedin_url: str) -> list[float]: 
    '''
    Takes a LinkedIn URL, parses the job description, and returns a list of scores for each resume
    in the database. 
    
    Parameters
    ----------
    linkedin_url : str
        the url of the job posting

    Returns
    -------
        list[float]
            list of scores for each resume
    '''
    job_description = JobParser.__call__(linkedin_url).get_str()

    resumes = get_data_json(get_db())["resumes"]
    rscores = {}
    rs = []
    for entry in resumes: 
        if entry["file_name"] != "None": 
            rscores[entry["file_name"]] = Analyzer.get_score(entry["raw_text"], job_description)
            rs.append(rscores[entry["file_name"]] )
    
    return rs

@_app.on_event("shutdown")
def shutdown_event():
    """ Close database on server shutdown """
    db.close()


