from fastapi import FastAPI
from Database import *
from Analyzer import Analyzer
from JobParser import JobParser

# Store user data locally 
user_data_dir = ".resumatch"

# Fast API App 
app = FastAPI()

# Level DB local database 
db = get_data(user_data_dir)

def get_db(): 
    if db.closed: 
        return get_data(user_data_dir)
    return db

@app.post("/resume_names")
def _get_resume_names(): 
    return get_resume_names(get_db())

@app.post("/resumes")
def _get_data_json(): 
    return get_data_json(get_db())["resumes"]

@app.post("/add_resume")
def _add_resume(resume_file_path): 
    return add_resume(get_db(), resume_file_path)

# Add a remove resume 
@app.get("/remove_resume")
def _remove_resume(resume_file_name): 
    return remove_resume(get_db(), resume_file_name)

@app.get("/scores")
def _scores(linkedin_url): 
    job_description = JobParser.__call__(linkedin_url).get_str()

    resumes = get_data_json(get_db())["resumes"]
    rscores = {}
    rs = []
    for entry in resumes: 
        if entry["file_name"] != "None": 
            rscores[entry["file_name"]] = Analyzer.get_score(entry["raw_text"], job_description)
            rs.append(rscores[entry["file_name"]] )
    
    return rs

@app.on_event("shutdown")
def shutdown_event():
    db.close()

# @app.on_event("startup")
# def startup_event():
#     db = get_data(user_data_dir)
