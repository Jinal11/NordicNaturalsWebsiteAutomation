"""
***** Element class for HomePage ********
"""


class ElementsPage:
    def __init__(self, driver):
        self.driver = driver

    def find_URL_tag(self):
        # identify elements with tag name <a>
        return self.driver.find_elements_by_tag_name("a")
