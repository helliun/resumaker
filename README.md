To use the ResumeGenerator class that is defined in the resumaker.py module, follow these steps:

1. Import the ResumeGenerator class by adding the statement from resumaker import ResumeGenerator to the top of your python file.
2. Initialize the ResumeGenerator object by providing it three strings, one for personal info, and two for education info and work experience info, respectively. e.g., rg = ResumeGenerator(personal_info_str, education_info_str, work_experience_str)
3. You can call the generate_pdf_resume() method of the object to create a pdf file of the resume which can be saved and printed. rg.generate_pdf_resume()
4. Alternatively, you can call the send_resume_email() method of the object to email the resume as a pdf attachment. rg.send_resume_email()

Note: To use the email feature, you need to fill in your email credentials such as SMTP server, port, username, and password in the method definition. Also, ensure that the email sender's address is authorized to send emails using your SMTP server.