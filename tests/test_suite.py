import unittest
from tests.login.login_test import LoginTest
from tests.home.home_test import HomeTest
from tests.resources.resource_test import ResourceTest
from tests.project.project_test import ProjectTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(HomeTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(ResourceTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(ProjectTest)
tsuite = unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(tsuite)