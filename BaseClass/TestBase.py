"""
************** This is base class, So here we will handle setup and teardown methods ***********
Import selenium web driver for website automation
Import unittest to run all test_cases cases / Test Suite
"""

from selenium import webdriver
import time
import unittest


class SetUpClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            # Import Chrome web driver (we can add more web driver here or can create a separate file for web drivers)
            cls.driver = webdriver.Chrome(executable_path="../BaseClass/chromedriver")
            cls.driver.maximize_window()
            cls.driver.get("https://www.nordicnaturals.com/consumers/")
            time.sleep(30)
            pass
        except:
            print("Something went wrong! Check your internet connection!!")



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

