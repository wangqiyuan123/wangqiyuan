from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
wd = webdriver.Chrome()
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# elements = wd.find_elements(By.TAG_NAME,"span")
# elements.send_keys("通讯")
elements=wd.find_elements(By.ID,"container")
# element=wd.find_element(By.ID,"go")
# element.click()

for element in elements:
    print(element.text)
input()
