from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

class GoogleCareersPageModel(object):

    def __init__(self, driver, wait_time = 10):
        # Local driver instance
        self.__browser = driver
        # Individual Page Models
        self.google_careers_home_page = GoogleCareersHomePage(self.__browser, wait_time)
        self.google_jobs_page = GoogleJobsPage(self.__browser, wait_time)
        self.google_job_post_page = GoogleJobPostPage(self.__browser, wait_time)
        self.google_gmail_login_page = GoogleGmailLoginPage(self.__browser, wait_time)
        self.google_job_application_page = GoogleJobApplicationPage(self.__browser, wait_time)

    def go_to_job_list(self):
        self.google_careers_home_page.jobs_button().click()

    def select_job_by_index(self, index = 0):
        self.google_jobs_page.get_job_list()[index].click()

    def apply_to_job(self):
        self.google_job_post_page.apply_button().click()

    def switch_to_job_application_frame(self):
        self.__browser.driver.switch_to_window(self.__browser.driver.window_handles[1])

    def get_application_status(self):
        return self.google_job_application_page.get_application_status_text()

    def edit_job_application(self):
        self.google_job_application_page.edit_application_button().click()

    def login_gmail_account(self, mail, password):
        self.google_gmail_login_page.email_edit().send_keys(mail)
        self.google_gmail_login_page.next_button().click()
        time.sleep(2)
        self.google_gmail_login_page.password_edit().send_keys(password)
        time.sleep(1)
        self.google_gmail_login_page.login_button().click()

    def submit_resume(self, resume_name):
        current_frame = self.__browser.driver.current_window_handle
        try:
            self.google_job_application_page.delete_attachment_button().click()
        except:
            pass
        self.google_job_application_page.select_file_button().click()
        time.sleep(2)
        self.__browser.driver.switch_to_frame(self.google_job_application_page.resume_file_frame())
        time.sleep(2)
        self.google_job_application_page.google_drive_button().click()
        ActionChains(self.__browser.driver).double_click(
            self.google_job_application_page.select_file_from_google_drive_option(resume_name)
        ).perform()
        time.sleep(2)
        self.__browser.driver.switch_to_window(current_frame)

    def fill_contact_details(self, name, country, city, email):
        # Get ActionChains class for use during all the method
        action = ActionChains(self.__browser.driver)
        legal_name = self.google_job_application_page.legal_name_edit()
        action.move_to_element(self.google_job_application_page.legal_name_edit()).perform()
        legal_name.clear()
        legal_name.send_keys(name)
        contact_country = self.google_job_application_page.country_region_edit()
        action.move_to_element(contact_country).perform()
        contact_country.send_keys(country)
        contact_city = self.google_job_application_page.city_edit()
        action.move_to_element(contact_city).perform()
        contact_city.clear()
        contact_city.send_keys(city)
        contact_email = self.google_job_application_page.email_edit()
        action.move_to_element(contact_email).perform()
        contact_email.clear()
        contact_email.send_keys(email)

    def fill_education(self, education_number, university, degree, status, major, country):
        # Get ActionChains class for use during all the method
        action = ActionChains(self.__browser.driver)
        # Start filling the application
        attended_university = self.google_job_application_page.attended_university_yes_radiobutton()
        action.move_to_element(attended_university).perform()
        attended_university.click()
        school_name = self.google_job_application_page.school_name_edit(education_number)
        action.move_to_element(school_name).perform()
        school_name.clear()
        school_name.send_keys(university)
        time.sleep(1)
        school_name.send_keys(Keys.DOWN)
        school_name.send_keys(Keys.RETURN)
        degree_type = self.google_job_application_page.degree_type_edit(education_number)
        action.move_to_element(degree_type).perform()
        degree_type.send_keys(degree)
        degree_status = self.google_job_application_page.degree_status_edit(education_number)
        action.move_to_element(degree_status).perform()
        degree_status.send_keys(status)
        area_of_study = self.google_job_application_page.degree_major_edit(education_number)
        action.move_to_element(area_of_study).perform()
        area_of_study.clear()
        area_of_study.send_keys(major)
        country_education = self.google_job_application_page.degree_country_edit(education_number)
        action.move_to_element(country_education).perform()
        country_education.send_keys(country)

    def remove_all_degrees(self):
        all_removed = False
        while not all_removed:
            try:
                self.google_job_application_page.remove_degree_button(0).click()
            except:
                all_removed = True

    def fill_work_experience(self, position_number, employer, title, start_date_month, start_date_year, end_date_month,
                             end_date_year, country, city, current_job = True):
        # Get ActionChains class for use during all the method
        action = ActionChains(self.__browser.driver)
        # Start filling the application
        first_job = self.google_job_application_page.first_job_no_radiobutton()
        action.move_to_element(first_job).perform()
        first_job.click()
        employer_name = self.google_job_application_page.employer_name_edit(position_number)
        action.move_to_element(employer_name).perform()
        employer_name.clear()
        employer_name.send_keys(employer)
        job_title = self.google_job_application_page.job_title_edit(position_number)
        action.move_to_element(job_title).perform()
        job_title.clear()
        job_title.send_keys(title)
        start_month = self.google_job_application_page.start_month_edit(position_number)
        action.move_to_element(start_month).perform()
        start_month.send_keys(start_date_month)
        start_year = self.google_job_application_page.start_year_edit(position_number)
        action.move_to_element(start_year).perform()
        start_year.clear()
        start_year.send_keys(start_date_year)
        current_job_check = self.google_job_application_page.current_job_checkbox(position_number)
        action.move_to_element(current_job_check).perform()
        if current_job:
            if current_job_check.get_attribute('aria-checked') == 'false':
                current_job_check.click()
        else:
            if current_job_check.get_attribute('aria-checked') == 'true':
                current_job_check.click()
            end_month = self.google_job_application_page.end_month_edit(position_number)
            action.move_to_element(end_month).perform()
            end_month.send_keys(end_date_month)
            end_year = self.google_job_application_page.end_year_edit(position_number)
            action.move_to_element(end_year).perform()
            end_year.clear()
            end_year.send_keys(end_date_year)
        country_job = self.google_job_application_page.work_country_edit(position_number)
        action.move_to_element(country_job).perform()
        country_job.send_keys(country)
        city_job = self.google_job_application_page.work_city_edit(position_number)
        action.move_to_element(city_job).perform()
        city_job.clear()
        city_job.send_keys(city)

    def add_another_job(self):
        self.google_job_application_page.add_another_job_button().click()

    def remove_all_jobs(self):
        all_removed = False
        while not all_removed:
            try:
                self.google_job_application_page.remove_job_button(0).click()
            except:
                all_removed = True

class GoogleCareersBasePage(object):

    def __init__(self, driver, wait_time = 10):
        self.__browser = driver
        self.__wait_time = wait_time

    def jobs_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@data-ga-label="Jobs"]')))

    def fields_of_work_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@data-ga-label="Fields of work"]')))

    def locations_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@data-ga-label="Locations"]')))

    def how_we_hire_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@data-ga-label="How we hire"]')))

    def students_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@data-ga-label="Students"]')))


class GoogleCareersHomePage(GoogleCareersBasePage):

    def __init__(self, driver, wait_time = 10):
        self.__browser = driver
        self.__wait_time = wait_time
        super().__init__(self.__browser, self.__wait_time)

    def search_jobs_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.NAME, 'n')))


class GoogleJobsPage(GoogleCareersBasePage):

    def __init__(self, driver, wait_time = 10):
        self.__browser = driver
        self.__wait_time = wait_time
        super().__init__(self.__browser)

    def search_jobs_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[contains(@role, "search")]')))

    def get_job_list(self):
        job_board = self.__browser.driver.find_element_by_class_name(
            'GXRRIBB-I-e'
        )
        # Get the direct children
        job_list = job_board.find_elements_by_xpath("./*")
        # Finally, return the list
        return job_list


class GoogleJobPostPage(GoogleCareersBasePage):

    def __init__(self, driver, wait_time = 10):
        self.__browser = driver
        self.__wait_time = wait_time
        super().__init__(self.__browser)

    def apply_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'apply')))


class GoogleGmailLoginPage(object):

    def __init__(self, driver, wait_time = 10):
        self.__wait_time = wait_time
        self.__browser = driver

    def email_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.ID, "identifierId")))

    def next_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.ID, "identifierNext")))

    def password_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.NAME, "password")))

    def login_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.ID, "passwordNext")))


class GoogleJobApplicationPage(object):

    def __init__(self, driver, wait_time = 10):
        self.__wait_time = wait_time
        self.__browser = driver

    def get_application_status_text(self):
        status_title = WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*/h1[@aria-live="assertive"]')))
        counter = 0
        while counter < 2:
            try:
                WebDriverWait(self.__browser.driver, 0.5).until(
                    expected_conditions.text_to_be_present_in_element((By.XPATH, '//*/h1[@aria-live="assertive"]'), 'Review your application')
                )
                break
            except exceptions.TimeoutException: pass

            try:
                found = WebDriverWait(self.__browser.driver, 0.5).until(
                    expected_conditions.text_to_be_present_in_element((By.XPATH, '//*/h1[@aria-live="assertive"]'), 'Complete application')
                )
                break
            except exceptions.TimeoutException: pass
            counter += 1
        return status_title.text

    def edit_application_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/button[contains(text(), "Edit application")]')))

    def select_file_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((By.ID, "resume-upload-button")))

    def delete_attachment_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/button[@aria-label="Delete attachment"]')))

    def resume_file_frame(self):
        frame_list = self.__browser.driver.find_elements(By.TAG_NAME, "iframe")
        for frame in frame_list:
            if frame.get_attribute('class') == "picker-frame":
                return frame

    def google_drive_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/div[@id=":6"]')))

    def list_view_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/div[@aria-label="List view"]'
            ))
        )

    def select_file_from_google_drive_option(self, resume_name):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.element_to_be_clickable((
                By.XPATH, '//*/span[contains(text(), "' + resume_name + '")]'
            ))
        )

    def legal_name_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'input_1')))

    def preferred_name_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'preferred-name')))

    def country_region_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'contactInfoCountry')))

    def city_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'contactInfoCity')))

    def state_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'input_268')))

    def zipcode_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'input_6')))

    def email_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'email-0')))

    def email_edit(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'phone-0')))

    def attended_university_yes_radiobutton(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'radio_8')))

    def school_name_edit(self, school_name_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'school-name-' + str(school_name_number))))

    def degree_type_edit(self, degree_type_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'degreeType' + str(degree_type_number))))

    def degree_status_edit(self, degree_status_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'degree-status-' + str(degree_status_number))))

    def degree_major_edit(self, degree_major_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'degreeMajor' + str(degree_major_number))))

    def degree_country_edit(self, degree_country_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'degreeCountry' + str(degree_country_number))))

    def remove_degree_button(self, degree_counter = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/div[' + str(degree_counter + 1) + ']/button[contains(text(), "Remove this degree")]')))

    def add_another_degree_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/button[contains(text(), "Add another degree")]')))

    def first_job_no_radiobutton(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'radio_11')))

    def employer_name_edit(self, employer_name_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.ID, 'work-name-' + str(employer_name_number))))

    def job_title_edit(self, job_title_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'jobTitle' + str(job_title_number))))

    def start_month_edit(self, start_month_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'startMonth' + str(start_month_number))))

    def start_year_edit(self, start_year_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'start-year-' + str(start_year_number))))

    def current_job_checkbox(self, checkbox_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/div[' + str(checkbox_number+1) + ']/div[2]/md-checkbox[@aria-label="This is your current job"]'
            ))
        )

    def end_month_edit(self, end_month_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'endMonth' + str(end_month_number))))


    def end_year_edit(self, end_year_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'end-year-' + str(end_year_number))))

    def work_country_edit(self, work_country_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'workCountry' + str(work_country_number))))

    def work_city_edit(self, work_city_number = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.NAME, 'workCity' + str(work_city_number))))

    def add_another_job_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/button[contains(text(), "Add another job")]')))

    def next_button(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/button[contains(text(), "Next")]')))

    def past_end_date_error_text(self):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/div[contains(text(), "End date cannot come before start date")]')))

    def remove_job_button(self, job_counter = 0):
        return WebDriverWait(self.__browser.driver, self.__wait_time).until(
            expected_conditions.presence_of_element_located((
                By.XPATH, '//*/div[' + str(job_counter + 1) + ']/button[contains(text(), "Remove this job")]')))