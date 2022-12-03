import plyvel
import json
import os

from .ResumeParser import ResumeParser

# Retrive saved user data
def get_data(user_data_dir : str) -> plyvel.DB: 
    ''' Load in local LevelDB database
    
    Parameters
    ----------
    user_data_dir : str
        The directory where the user's data is stored.
    
    Returns
    -------
        A plyvel.DB object.
    
    '''

    db = plyvel.DB(user_data_dir, create_if_missing=True)

    user_data_dict = db.get(b'user_data_dict')

    if user_data_dict is None: 
        user_data_dict = {"user_id": "", 
                          "resumes": [{"file_name": "None"}]}

        db.put(b'user_data_dict', json.dumps(user_data_dict).encode())

    return db

def get_data_json(db: plyvel.DB) -> dict: 
    ''' Get user data as json dict from databse
    
    Parameters
    ----------
    db : plyvel.DB
        LevelDB databse
    
    Returns
    -------
        A dictionary of the user data.
    
    '''

    return json.loads(db.get(b'user_data_dict'))

def get_resume_names(db: plyvel.DB) -> list[str]:
    ''' Get list of resume names stored in DB
    
    Parameters
    ----------
    db : plyvel.DB
        the database object
    
    Returns
    -------
        A list of resume names.
    
    '''

    user_data_dict = get_data_json(db)
    names = []
    for r in user_data_dict["resumes"]: 
        if r["file_name"] != "None": 
            names.append(r["file_name"])
    return names

def add_resume(db: plyvel.DB, resume_file_path: str):
    ''' Takes a resume file path, parses the resume, and adds the resume to the database
    
    Parameters
    ----------
    db : plyvel.DB
        The database object that we created earlier.
    resume_file_path : str
        The path to the resume file.
    
    '''

    user_data_dict = get_data_json(db)

    resume_data = {"file_name" : os.path.basename(resume_file_path), 
                   "raw_text": ResumeParser.get_raw_text(resume_file_path)}

    user_data_dict["resumes"].append(resume_data)

    db.put(b'user_data_dict', json.dumps(user_data_dict).encode())

def remove_resume(db: plyvel.DB, resume_file_name: str):
    '''
    Removes a resume from the database. 
    
    Parameters
    ----------
    db : plyvel.DB
        the database object
    resume_file_name : str
        The name of the resume file you want to remove.
    
    '''

    user_data_dict = get_data_json(db)
    resumes = user_data_dict["resumes"]

    for i, r in enumerate(resumes): 
        if r["file_name"] == resume_file_name: 
            resumes.pop(i)

    user_data_dict["resumes"] = resumes

    db.put(b'user_data_dict', json.dumps(user_data_dict).encode())
    