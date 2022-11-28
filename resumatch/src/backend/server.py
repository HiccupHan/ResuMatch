from fastapi import FastAPI
from Database import *
from Analyzer import Analyzer

# Store user data locally 
user_data_dir = "./.resumatch"

# Fast API App 
app = FastAPI()

# Level DB local database 
db = get_data(user_data_dir)

@app.post("/resume_names")
def _get_resume_names(): 
    return get_resume_names(db)

@app.post("/resumes")
def _get_data_json(): 
    return get_data_json(db)

@app.post("/add_resume")
def _add_resume(resume_file_path): 
    return add_resume(db, resume_file_path)

@app.post("/scores")
def _scores(job_description): 
    resumes = get_data_json(db)["resumes"]
    return {entry["file_name"]:Analyzer.get_score(entry["raw_text"], job_description) for entry in resumes}


db.close()
