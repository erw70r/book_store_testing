import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")
ruby = driver.find_element(By.XPATH, "//img[@title='Selenium Ruby']")
ruby.click()

reviews = driver.find_element(By.CLASS_NAME, "reviews_tab")
reviews.click()
star = driver.find_element(By.CLASS_NAME, "star-5")
star.click()

comment = driver.find_element(By.ID, "comment")
comment.send_keys("Nice book!")
name = driver.find_element(By.ID, "author")
name.send_keys("erw70r")
email = driver.find_element(By.ID, "email")
email.send_keys("erw70r@gmail.com")
submit = driver.find_element(By.ID, "submit")
submit.click()

driver.quit()