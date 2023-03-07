#requirements: none

# imports
from resumaker import ResumeGenerator


# code
def main():
    personal_info_str = "John Smith, 103 Main St, jsmith@example.com, 555-555-5555, profile.jpg"
    education_info_strs = ["Bachelor of Science, MIT, May 2010", "Master of Science, Harvard University, May 2012"]
    work_experience_info_strs = ["Software Engineer, Google, Jan 2013 - Jan 2016", "Senior Software Engineer, Amazon, Feb 2016 - current"]
    resume = ResumeGenerator(personal_info_str, education_info_strs, work_experience_info_strs)
    resume.generate_pdf_resume()
    resume.send_resume_email()


if __name__ == "__main__":
    main()