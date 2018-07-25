# Adding a comment on the top

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from ui_testing.careertests.tests import GoogleCareerTests

suite = unittest.TestSuite()
suite.addTest(GoogleCareerTests('test00001_modify_end_date_with_current_job_marked'))
suite.addTest(GoogleCareerTests('test00002_job_application_let_user_continue_with_wrong_date'))
runner = unittest.TextTestRunner()
runner.run(suite)
