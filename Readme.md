# CS130 Project
### Team members: Jagrit Digani, Junkai Zhang, Yuanzhou Chen, Xuanzhe Han, Qiwei Di, Yiwen Kou

# ResuMatch
### a chrome extension that matches your resume to LinkedIn job postings. Built with React

## Installation instructions 

### Download the release files, `cd resumatch` and run `npm install`

The command will install all missing dependencies.

### Build the app with `npm run build:prod`

Builds the app for production to the `dist` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

### Load into Chrome browser

Open Chrome extension page, turn on developer mode, then click `Load Unpacked` and load the dist folder. 

### Setup on server side 

Set up conda virtual environment using 
(Note: install conda on your system https://docs.conda.io/en/latest/)\
`conda create -n resumatch python=3.10`\
`conda activate resumatch`\
`conda install -c conda-forge spacy`\
`conda install sphinx`\
`pip install sphinx-rtd-theme`\
`pip install streamlit`\
`pip install spacy-streamlit`\
`pip install plyvel`\
`pip install "fastapi[all]`\
`pip install requests_html`


Then download the necessary files and models for the NLP analysis \
`python -m spacy download en_core_web_lg`\
`python -m spacy download en_core_web_sm`

Launch backend server using \
`cd resumatch/src/backend/` \
`uvicorn server:app --reload`

Launch webapp using (from resumatch dir) \
`streamlit run src/ResuMatch.py ` \