"""
********** blueprint file *********
-----------------------------------------
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/Jinal/PycharmProjects/NordicNaturals/chromedriver")
driver.maximize_window()
driver.get("https://www.nordicnaturals.com/consumers/")

time.sleep(30)
# traverse list
result_array = []
invalid_url = []
# identify elements with tagname <a>
alldata = driver.find_elements_by_tag_name("a")
for lnk in alldata:
    all_url = lnk.get_attribute("href")
    print(all_url)

    result_array.append(all_url)
    print(len(result_array))

for i in range(0, len(result_array)):
    print(i)
    try:
        # x = int(input("Please enter a number: "))
        driver.get(result_array[i])
        r = requests.get(result_array[i])
        print(r.status_code)
        # time.sleep(10)
        if r.status_code == 404:
           print("404 Error found")
        print("Done everything")
        pass
    except:
        print("Oops!  Invalid URL.  Try again...")
        invalid_url.append(result_array[i])
        # driver.get("https://www.nordicnaturals.com/consumers/")

driver.quit()

"""