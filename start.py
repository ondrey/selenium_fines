from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\guest\\AppData\\Local\\Google\\Chrome\\User Data")

# Указываем полный путь к geckodriver.exe на вашем ПК.
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.get("https://гибдд.рф/check/fines")


elem = driver.find_element_by_id('checkFinesRegnum')
elem.send_keys('У***ТР')
elem = driver.find_element_by_id('checkFinesRegreg')
elem.send_keys('93')

time.sleep(4)
elem = driver.find_element_by_id('checkFinesStsnum')
elem.click()
elem.send_keys('23****10')


elem = driver.find_element_by_link_text('запросить проверку')
elem.click()

elem = driver.find_element_by_class_name('checkResult')
print(elem.text)