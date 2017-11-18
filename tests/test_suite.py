import unittest
from tests.login.login_test import LoginTest
from tests.home.home_test import HomeTest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(HomeTest)

tsuite = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(tsuite)