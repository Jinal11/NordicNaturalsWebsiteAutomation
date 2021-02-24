"""
********** Test Cases for Home Page *********
"""
import unittest
from ActionClass.HomePageActions import HomePageActions
from BaseClass.TestBase import SetUpClass


class VerifyHomePageLinks(SetUpClass):
    def test_links(self):
        links = HomePageActions(self.driver)
        links.get_URL()
        links.verify_links()


if __name__ == '__main__':
    unittest.main()
