#requirements: os, re, reportlab, smtplib

# imports
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


# code
class ResumeGenerator:
    def __init__(self, personal_info_str, education_info_strs, work_experience_info_strs):
        self.personal_info_dict = self._parse_personal_info(personal_info_str)
        self.education_info_dict = self._parse_education_info(education_info_strs)
        self.work_experience_info_dict = self._parse_work_experience_info(work_experience_info_strs)

    def generate_pdf_resume(self):
        pdf_file = canvas.Canvas('resume.pdf', pagesize=letter)
        pdf_file.drawString(1*inch, 10.5*inch, f"Name: {self.personal_info_dict['Name']}")
        pdf_file.drawString(1*inch, 10*inch, f"Address: {self.personal_info_dict['Address']}")
        pdf_file.drawString(1*inch, 9.5*inch, f"Email: {self.personal_info_dict['Email']}")
        pdf_file.drawString(1*inch, 9*inch, f"Phone: {self.personal_info_dict['Phone']}")
        if os.path.exists(self.personal_info_dict['Profile Image']):
            pdf_file.drawImage(self.personal_info_dict['Profile Image'], 5*inch, 8*inch, width=2*inch, height=2*inch)
        pdf_file.drawString(1*inch, 7*inch, 'Education:')
        y_position = 6.75*inch
        for info in self.education_info_dict['Education']:
            pdf_file.drawString(1.25*inch, y_position, 'Degree: ' + info['degree'])
            pdf_file.drawString(1.25*inch, y_position-0.25*inch, 'School: ' + info['school'])
            pdf_file.drawString(1.25*inch, y_position-0.5*inch, 'Date: ' + info['date'])
            y_position -= 0.75*inch
        pdf_file.drawString(1*inch, y_position, 'Work Experience:')
        y_position -= 0.5*inch
        for info in self.work_experience_info_dict['Work Experience']:
            pdf_file.drawString(1.25*inch, y_position, 'Title: ' + info['title'])
            pdf_file.drawString(1.25*inch, y_position-0.25*inch, 'Company: ' + info['company'])
            pdf_file.drawString(1.25*inch, y_position-0.5*inch, 'Date: ' + info['date'])
            y_position -= 0.75*inch
        pdf_file.save()
    
    def send_resume_email(self):
        msg = MIMEMultipart()
        msg['From'] = 'sender_email@example.com'
        msg['To'] = self.personal_info_dict['Email']
        msg['Subject'] = 'Resume'
        with open('resume.pdf', 'rb') as f:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(f.read())
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename('resume.pdf'))
            msg.attach(attachment)
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        smtp_username = 'your_username'
        smtp_password = 'your_password'
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.ehlo()
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)
        smtp_connection.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp_connection.quit()
    
    @staticmethod
    def _parse_personal_info(info_string):
        personal_info = {}
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        email = re.findall(email_pattern, info_string)
        phone = re.findall(phone_pattern, info_string)
        info = info_string.split(',')
        personal_info['Name'] = info[0].strip()
        personal_info['Email'] = email[0].strip()
        personal_info['Address'] = info[1].strip()
        personal_info['Phone'] = phone[0].strip()
        personal_info['Profile Image'] = info[2].strip()
        return personal_info
    
    @staticmethod
    def _parse_education_info(info_strings):
        education_info = {}
        education = []
        for info in info_strings:
            degree, school, date = info.split(',')
            education.append({'degree': degree.strip(),
                               'school': school.strip(),
                               'date': date.strip()})
        education_info['Education'] = education
        return education_info
    
    @staticmethod
    def _parse_work_experience_info(info_strings):
        work_experience_info = {}
        work_experience = []
        for info in info_strings:
            title, company, date = info.split(',')
            work_experience.append({'title': title.strip(),
                                     'company': company.strip(),
                                     'date': date.strip()})
        work_experience_info['Work Experience'] = work_experience
        return work_experience_info