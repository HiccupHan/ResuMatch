from fastapi import FastAPI
from Database import *
from Analyzer import Analyzer

# Store user data locally 
user_data_dir = "./.resumatch"

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
    return get_data_json(get_db())

@app.post("/add_resume")
def _add_resume(resume_file_path): 
    return add_resume(get_db(), resume_file_path)

# Add a remove resume 

@app.post("/scores")
def _scores(linkedin_url): 
    resumes = get_data_json(get_db())["resumes"]
    job_description = ""
    return {entry["file_name"]:Analyzer.get_score(entry["raw_text"], job_description) for entry in resumes}

@app.on_event("shutdown")
def shutdown_event():
    db.close()

# @app.on_event("startup")
# def startup_event():
#     db = get_data(user_data_dir)
