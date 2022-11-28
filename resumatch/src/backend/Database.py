import plyvel
import json
import os

from ResumeParser import ResumeParser

# Retrive saved user data
def get_data(user_data_dir : str): 
    db = plyvel.DB(user_data_dir, create_if_missing=True)

    user_data_dict = db.get(b'user_data_dict')

    if user_data_dict is None: 
        user_data_dict = {"user_id": "", 
                          "resumes": [{"file_name": "None"}]}

        db.put(b'user_data_dict', json.dumps(user_data_dict).encode())

    return db

def get_data_json(db): 
    return json.loads(db.get(b'user_data_dict'))

def get_resume_names(db):
    user_data_dict = get_data_json(db)
    names = []
    for r in user_data_dict["resumes"]: 
        if r["file_name"] != "None": 
            names.append(r["file_name"])
    return names

def add_resume(db, resume_file_path):
    user_data_dict = get_data_json(db)

    print(user_data_dict)

    resume_data = {"file_name" : os.path.basename(resume_file_path), 
                   "raw_text": ResumeParser.get_raw_text(resume_file_path)}

    user_data_dict["resumes"].append(resume_data)

    print(user_data_dict)

    db.put(b'user_data_dict', json.dumps(user_data_dict).encode())
    