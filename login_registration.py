# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.ID, "menu-item-50")
# my_account.click()
#
# email = driver.find_element(By.ID, "reg_email")
# email.send_keys("erw70r@gmail.com")
# password = driver.find_element(By.ID, "reg_password")
# password.send_keys("erw13123=q")
# register = driver.find_element(By.NAME, "register")
# register.click()

#driver.quit()


#######Задание2

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")

my_account = driver.find_element(By.ID, "menu-item-50")
my_account.click()

email = driver.find_element(By.ID, "username")
email.send_keys("erw70r@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("erw13123=q")
login = driver.find_element(By.NAME, "login")
login.click()

logout = driver.find_element(By.CLASS_NAME, "woocommerce-MyAccount-navigation-link--customer-logout")
logout_text = logout.text
assert logout_text =="Logout"

driver.quit()

