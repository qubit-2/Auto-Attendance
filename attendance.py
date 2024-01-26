from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://eduserver.nitc.ac.in/login/index.php')

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('')
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('')
button = driver.find_element_by_xpath('//*[@id="region-main"]/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/button')
button.click()

time.sleep(4)
#for pressing ENTER
box.send_keys(Keys.RETURN)
attendance = driver.find_element_by_link_text('Attendance')
attendance.click()
#For go to activity
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Go to activity'))
    )
    element.click()
except:
    driver.quit()
#For submitting attendance
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Submit attendance'))
    )
    element.click()
#present mark
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id_status_6020"]'))
    )
    element.click()
#press save changes
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id_submitbutton"]'))
    )
    element.click()

except:
    driver.quit()

#ac = driver.find_element_by_link_text('Go to activity')
#ac.click()

#submit = driver.find_element_by_link_text('Submit attendance')
#submit.click()

#logout = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1617527413962_60"]/div/div/div[3]/div[2]/a')
#logout.click()
