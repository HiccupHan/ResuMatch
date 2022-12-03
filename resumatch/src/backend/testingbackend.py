import unittest
from ResumeParser import ResumeParser
import spacy
from spacypdfreader import pdf_reader
from JobParser import JobParser
from Analyzer import Analyzer
import Database

class TestBackend(unittest.TestCase):

    def test_ResumeParser(self):

        real_text_1 = pdf_reader(r'C:\Users\Douglas\Desktop\ResuMatch-main\resumatch\src\backend\backend_resume.pdf', spacy.load('en_core_web_sm')).text
        text_1 = ResumeParser.get_raw_text(file_path= r'..\img\backend_resume.pdf')
        self.assertEqual(real_text_1, text_1)

        real_text_2 = pdf_reader(r'C:\Users\Douglas\Desktop\ResuMatch-main\resumatch\src\backend\frontend_resume.pdf', spacy.load('en_core_web_sm')).text
        text_2 = ResumeParser.get_raw_text(file_path= r'..\img\frontend_resume.pdf')
        self.assertEqual(real_text_2, text_2)

    def test_JobParser(self):

        job_desc_1 = JobParser.__call__('https://www.linkedin.com/jobs/view/3362398129/?alternateChannel=search&refId=w04%2BrmxU5sro6vXifS34dg%3D%3D&trackingId=1y85aQ831OnEgK3F80n2fQ%3D%3D').get_str()
        self.assertIsInstance(job_desc_1, str)

        job_desc_2 = JobParser.__call__('https://www.linkedin.com/jobs/view/3359673205/?alternateChannel=search&refId=MrCnP1z9N7iOpmCzBEK2Ug%3D%3D&trackingId=adf9Xcj6jPfr7r5r24Zsuw%3D%3D').get_str()
        self.assertIsInstance(job_desc_2, str)
   

    def test_Analyzer(self):

        job_desc_1 = JobParser.__call__('https://www.linkedin.com/jobs/view/3362398129/?alternateChannel=search&refId=w04%2BrmxU5sro6vXifS34dg%3D%3D&trackingId=1y85aQ831OnEgK3F80n2fQ%3D%3D').get_str()
        JobParser.__call__('https://www.linkedin.com/jobs/view/3362398129/?alternateChannel=search&refId=w04%2BrmxU5sro6vXifS34dg%3D%3D&trackingId=1y85aQ831OnEgK3F80n2fQ%3D%3D').print()
        resu_desc_1 = ResumeParser.get_raw_text(file_path= r'..\img\backend_resume.pdf')
        score_1 = Analyzer.get_score(resu_desc_1, job_desc_1)
        self.assertIsInstance(score_1, float)


        job_desc_2 = JobParser.__call__('https://www.linkedin.com/jobs/view/3359673205/?alternateChannel=search&refId=MrCnP1z9N7iOpmCzBEK2Ug%3D%3D&trackingId=adf9Xcj6jPfr7r5r24Zsuw%3D%3D').get_str()
        JobParser.__call__('https://www.linkedin.com/jobs/view/3359673205/?alternateChannel=search&refId=MrCnP1z9N7iOpmCzBEK2Ug%3D%3D&trackingId=adf9Xcj6jPfr7r5r24Zsuw%3D%3D')
        resu_desc_2 = ResumeParser.get_raw_text(file_path= r'..\img\frontend_resume.pdf')
        score_2 = Analyzer.get_score(resu_desc_2, job_desc_2)
        self.assertIsInstance(score_2, float)


    def test_Database(self):

        db1 = Database.get_data(r'./db1/')
        Database.add_resume(db1, r'..\img\backend_resume.pdf')
        name1 = Database.get_resume_names(db1)[0]
        self.assertIsInstance(name1, str)

        db2 = Database.get_data(r'./db2/')
        Database.add_resume(db2, r'..\img\frontend_resume.pdf')
        name2 = Database.get_resume_names(db2)[0]
        self.assertIsInstance(name2, str)

if __name__ == '__main__':
    unittest.main()
