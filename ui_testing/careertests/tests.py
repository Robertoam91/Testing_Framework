from ui_testing.careertests import context
import time

class GoogleCareerTests(context.GoogleCareersContext):

    def test00001_modify_end_date_with_current_job_marked(self):
        # Open Google Jobs page and select a job to apply
        self.google_careers_model.go_to_job_list()
        self.google_careers_model.select_job_by_index(0)
        self.google_careers_model.apply_to_job()
        self.browser.driver.switch_to_window(self.browser.driver.window_handles[1])
        # Google account page will be opened, sign in with preferred credentials
        self.google_careers_model.login_gmail_account(self.google_careers_data.user_mail, self.google_careers_data.user_pass)
        # Now that you are logged in, check in which page you did begin
        # If you started at Complete Application, select Edit Application
        if self.google_careers_model.get_application_status() == 'Review your application':
            self.google_careers_model.edit_job_application()
        # Update resume
        self.google_careers_model.submit_resume(self.google_careers_data.user_resume_name)
        # Fill the contact information
        self.google_careers_model.fill_contact_details(self.google_careers_data.user_firstname + ' ' + self.google_careers_data.user_lastname,
                                                       self.google_careers_data.user_country,
                                                       self.google_careers_data.user_city,
                                                       self.google_careers_data.user_mail
                                                       )
        # Fill the education experience
        # If more than one degree is currently filled in the application, remove the extras
        self.google_careers_model.remove_all_degrees()
        self.google_careers_model.fill_education(0, self.google_careers_data.user_school_name,
                                                 self.google_careers_data.user_degree,
                                                 self.google_careers_data.user_degree_status,
                                                 self.google_careers_data.user_major,
                                                 self.google_careers_data.user_country
                                                 )
        # Fill the work experience information
        # This scenario will cover a past end date, but "Current Job" flag will be selected
        # Business flow should let the user continue, even if an invalid end date is entered
        self.google_careers_model.remove_all_jobs()
        self.google_careers_model.fill_work_experience(0, self.google_careers_data.user_employer_name1,
                                                       self.google_careers_data.user_job_title1,
                                                       self.google_careers_data.user_start_month1,
                                                       self.google_careers_data.user_start_year1,
                                                       self.google_careers_data.user_valid_end_month1,
                                                       self.google_careers_data.user_invalid_end_year1,
                                                       self.google_careers_data.user_country,
                                                       self.google_careers_data.user_city,
                                                       current_job = False)
        # Activate "Current Job" checkbox
        self.google_careers_model.google_job_application_page.current_job_checkbox(0).click()
        # And finally press NEXT
        self.google_careers_model.google_job_application_page.next_button().click()

        assert self.google_careers_model.get_application_status() == 'Review your application'
        assert self.google_careers_model.google_job_application_page.past_end_date_error_text().get_attribute('aria-hidden') == 'true'

    def test00002_job_application_let_user_continue_with_wrong_date(self):
        # Open Google Jobs page and select a job to apply
        self.google_careers_model.go_to_job_list()
        self.google_careers_model.select_job_by_index(0)
        self.google_careers_model.apply_to_job()
        self.browser.driver.switch_to_window(self.browser.driver.window_handles[1])
        # Google account page will be opened, sign in with preferred credentials
        self.google_careers_model.login_gmail_account(self.google_careers_data.user_mail, self.google_careers_data.user_pass)
        # Now that you are logged in, check in which page you did begin
        # If you started at Complete Application, select Edit Application
        if self.google_careers_model.get_application_status() == 'Review your application':
            self.google_careers_model.edit_job_application()
        # Update resume
        self.google_careers_model.submit_resume(self.google_careers_data.user_resume_name)
        # Fill the contact information
        self.google_careers_model.fill_contact_details(self.google_careers_data.user_firstname + ' ' + self.google_careers_data.user_lastname,
                                                       self.google_careers_data.user_country,
                                                       self.google_careers_data.user_city,
                                                       self.google_careers_data.user_mail
                                                       )
        # Fill the education experience
        # If more than one degree is currently filled in the application, remove the extras
        self.google_careers_model.remove_all_degrees()
        self.google_careers_model.fill_education(0, self.google_careers_data.user_school_name,
                                                 self.google_careers_data.user_degree,
                                                 self.google_careers_data.user_degree_status,
                                                 self.google_careers_data.user_major,
                                                 self.google_careers_data.user_country
                                                 )
        # Fill the work experience information
        # This scenario will cover a past end date in the second job
        # Business flow should not let the user continue
        self.google_careers_model.remove_all_jobs()
        self.google_careers_model.fill_work_experience(0, self.google_careers_data.user_employer_name1,
                                                       self.google_careers_data.user_job_title1,
                                                       self.google_careers_data.user_start_month1,
                                                       self.google_careers_data.user_start_year1,
                                                       self.google_careers_data.user_valid_end_month1,
                                                       self.google_careers_data.user_valid_end_year1,
                                                       self.google_careers_data.user_country,
                                                       self.google_careers_data.user_city,
                                                       current_job = False)
        # Add another job
        self.google_careers_model.add_another_job()
        # Fill the end date incorrectly (In the past)
        self.google_careers_model.fill_work_experience(1, self.google_careers_data.user_employer_name2,
                                                       self.google_careers_data.user_job_title2,
                                                       self.google_careers_data.user_start_month2,
                                                       self.google_careers_data.user_start_year2,
                                                       self.google_careers_data.user_valid_end_month2,
                                                       self.google_careers_data.user_invalid_end_year2,
                                                       self.google_careers_data.user_country,
                                                       self.google_careers_data.user_city,
                                                       current_job = False)

        # And finally press NEXT
        self.google_careers_model.google_job_application_page.next_button().click()

        assert self.google_careers_model.get_application_status() == 'Complete application'
        assert self.google_careers_model.google_job_application_page.past_end_date_error_text().get_attribute('aria-hidden') == 'false'
