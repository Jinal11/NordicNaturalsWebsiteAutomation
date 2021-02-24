"""
********* Perform all actions for the Home Page *************
"""

from Elements.HomePageElements import *
from pip._vendor import requests


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePageActions(BasePage):
    result_array = []
    invalid_url = []
    error_url = []

    def get_URL(self):
        alldata = ElementsPage(self.driver).find_URL_tag()
        for lnk in alldata:
            all_url = lnk.get_attribute("href")
            self.result_array.append(all_url)
        print("List for all links available on Home Page: ", self.result_array)
        print("Total Number of Links:", len(self.result_array))

    def verify_links(self):
        for i in range(0, len(self.result_array)):
            print("Verify the link:", self.result_array[i])
            try:
                self.driver.get(self.result_array[i])
                verify_link = requests.get(self.result_array[i])
                print("Status code for the Above link:", verify_link.status_code)
                # time.sleep(10)
                if verify_link.status_code == 404:
                    self.error_url.append(self.result_array[i])
                    print("404 Error found")
                    assert verify_link.status_code == "404", "all working"
                pass
            except:
                print("Oops!  Invalid URL.  Try again...")
                self.invalid_url.append(self.result_array[i])
        print("List of 404 ERROR Links:", self.error_url)
