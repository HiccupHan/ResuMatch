import streamlit as st
import plyvel
import json

# Store user data locally 
user_data_dir = "./.resumatch"

# Retrive saved user data
def get_data(user_data_dir : str): 
    db = plyvel.DB(user_data_dir, create_if_missing=True)

    user_data_dict = db.get(b'user_data_dict')

    if user_data_dict is None: 
        user_data_dict = {"user_id": "", 
                          "resumes": ["None"]}

        db.put(b'user_data_dict', json.dumps(user_data_dict).encode())
    else: 
        user_data_dict = json.loads(user_data_dict)

    return db


class Database: 
    db = get_data(user_data_dir)

    @staticmethod
    def get_db(): 
        if Database.db.closed: 
            Database.db = get_data(user_data_dir)

        return Database.db

def get_data_json(): 
    return json.loads(Database.get_db().get(b'user_data_dict'))

def get_resume_names():
    user_data_dict = get_data_json()
    st.session_state["resumes"] = user_data_dict["resumes"]
    return st.session_state["resumes"]

def add_resume(resume_file_path):
    user_data_dict = get_data_json()
    user_data_dict["resumes"].append(resume_file_path)
    Database.get_db().put(b'user_data_dict', json.dumps(user_data_dict).encode())
    st.session_state["resumes"] = get_resume_names()



def upload_page(): 
    
    st.title('ResuMatch')

    st.text("Welcome! Please upload a resume or select one that has already been uploaded")

    user_data_dict = get_data_json()

    for k, v in user_data_dict.items(): 
        if k not in st.session_state: 
            st.session_state[k] = v

    st.subheader("Upload Resume")
    resume_file = st.file_uploader("Resume", type="pdf")

    if st.button("Process file") and resume_file is not None: 
        file_name = resume_file.name
        add_resume(file_name)

    st.subheader("Select Resume")
    selection = st.selectbox("Uploaded Resumes", get_resume_names())



upload_page()
Database.db.close()