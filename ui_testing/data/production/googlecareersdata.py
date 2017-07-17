import datetime

#
# Product URLS
#
google_careers_home_url = "https://careers.google.com/"
google_jobs_url = "https://careers.google.com/jobs#t=sq&q=j&li=20&l=false&jcoid=7c8c6665-81cf-4e11-8fc9-ec1d6a69120c&jcoid=e43afd0d-d215-45db-a154-5386c9036525&"

#
# Test Data
#

# Job Information
user_desired_job = "Test Engineer"
user_desired_city = "Mountain View, CA, USA"

# Personal Information
user_firstname = "Roberto"
user_lastname = "Ayala"
user_country = "Mexico"
user_state = "Jalisco"
user_city = "Zapopan"
user_phone = "3313014449"
user_mail = "careertestbyrobert@gmail.com"
user_pass = "a1b2c3d4@"
user_resume_name = "Cool Resume.docx"

# Education
user_school_name = "Universidad Autonoma de Guadalajara"
user_degree = "Master"
user_degree_status = "Graduated"
user_major = "Computer Science"

# Employment
user_employer_name1 = "Cool Employer"
user_job_title1 = "Cool Engineer"
user_start_month1 = "March"
user_start_year1 = "2017"
user_valid_end_year1 = datetime.date.today().year
user_invalid_end_year1 = user_valid_end_year1 - 1
user_valid_end_month1 = datetime.date.today().strftime("%B")

user_employer_name2 = "Other Cool Employer"
user_job_title2 = "Smart Engineer"
user_start_month2 = "September"
user_start_year2 = "2012"
user_valid_end_year2 = "2017"
user_invalid_end_year2 = str(int(user_start_year1) - 1)
user_valid_end_month2 = "March"