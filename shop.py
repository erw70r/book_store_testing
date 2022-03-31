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
# email = driver.find_element(By.ID, "username")
# email.send_keys("erw70r@gmail.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("erw13123=q")
# login = driver.find_element(By.NAME, "login")
# login.click()
#
# shop = driver.find_element(By.ID, "menu-item-40")
# shop.click()
# html_forms = driver.find_element(By.XPATH, "//img[@title='Mastering HTML5 Forms']")
# html_forms.click()
# html5 = driver.find_element(By.TAG_NAME, "h1")
# html5_text = html5.text
# assert html5_text == "HTML5 Forms"
#
# driver.quit()



####### Задание 2


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.ID, "menu-item-50")
# my_account.click()
#
# email = driver.find_element(By.ID, "username")
# email.send_keys("erw70r@gmail.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("erw13123=q")
# login = driver.find_element(By.NAME, "login")
# login.click()
#
# shop = driver.find_element(By.ID, "menu-item-40")
# shop.click()
#
# number2 = driver.find_element(By.LINK_TEXT, "HTML")
# number2.click()
#
# elements = driver.find_elements(By.XPATH, "//a[@data-quantity='1']")
# print(len(elements))
#
# driver.quit()


####### Задание 3


# import time
# from selenium.webdriver.support.select import Select
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
# email = driver.find_element(By.ID, "username")
# email.send_keys("erw70r@gmail.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("erw13123=q")
# login = driver.find_element(By.NAME, "login")
# login.click()
#
# shop = driver.find_element(By.ID, "menu-item-40")
# shop.click()
#
# sort_selector = driver.find_element(By.NAME, "orderby")
# sort_selector_default = sort_selector.get_attribute("value")
# if sort_selector_default == "menu_order":
#     print("Cортировка по умолчанию")
# else:
#     print("Cортировка не по умолчанию")
#
# low = driver.find_element(By.NAME, "orderby")
# select = Select(low)
# select.select_by_index(5)
#
# sort_selector = driver.find_element(By.NAME, "orderby")
# sort_selector_low = sort_selector.get_attribute("value")
# if sort_selector_low == "price-desc":
#     print("Cортировка по уменьшению цены")
# else:
#     print("Cортировка не по уменьшению цены")
#
#
# driver.quit()


####### Задание 4


# import time
# from selenium.webdriver.support.select import Select
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
# email = driver.find_element(By.ID, "username")
# email.send_keys("erw70r@gmail.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("erw13123=q")
# login = driver.find_element(By.NAME, "login")
# login.click()
#
# shop = driver.find_element(By.ID, "menu-item-40")
# shop.click()
#
# android_book = driver.find_element(By.CSS_SELECTOR, ".post-169 h3")
# android_book.click()
#
# book_old_price = driver.find_element(By.CSS_SELECTOR, ".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element(By.CSS_SELECTOR, ".price > ins > span")
# book_new_price_text = book_new_price.text
#
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
#
# book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
#
# driver.quit()



####### Задание 5


# import time
# from selenium.webdriver.support.select import Select
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
# shop = driver.find_element(By.ID, "menu-item-40")
# shop.click()
#
# add_web = driver.find_element(By.XPATH, "//a[@data-product_id='182']")
# add_web.click()

# items = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents .cartcontents")
# items_text = items.text
# assert items_text == "1 Item"
# price = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents .amount")
# price_text = price.text
# assert price_text == "₹180.00"
# time.sleep(2)
# cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
# cart.click()
#
# subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
# total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00"))
#
# driver.quit()


####### Задание 6


# import time
# from selenium.webdriver.support.select import Select
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
# shop = driver.find_element(By.ID, "menu-item-40")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
#
# add_web = driver.find_element(By.XPATH, "//a[@data-product_id='182']")
# add_web.click()
# time.sleep(3)
# add_js_data = driver.find_element(By.XPATH, "//a[@data-product_id='180']")
# add_js_data.click()
#
# cart_btn = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
# cart_btn.click()
# time.sleep(3)
# remove_btn = driver.find_element(By.CLASS_NAME, "remove")
# remove_btn.click()
# undo_btn = driver.find_element(By.LINK_TEXT, "Undo?")
# undo_btn.click()
#
# quantity = driver.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(1) .product-quantity input")
# quantity.clear()
# quantity.send_keys("3")
#
# update_basket = driver.find_element(By.NAME, "update_cart")
# update_basket.click()
#
# quantity = driver.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(1) .product-quantity input")
# quantity_value = quantity.get_attribute("value")
# assert quantity_value == "3"
# time.sleep(3)
# apply_coupon = driver.find_element(By.NAME, "apply_coupon")
# apply_coupon.click()
#
# enter_code = driver.find_element(By.CLASS_NAME, "woocommerce-error")
# enter_code_text = enter_code.text
# assert enter_code_text == "Please enter a coupon code."
#
# driver.quit()



####### Задание 7


import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element(By.ID, "menu-item-40")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")

add_web = driver.find_element(By.XPATH, "//a[@data-product_id='182']")
add_web.click()
time.sleep(2)
cart_btn = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
cart_btn.click()

checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()

first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Dmitriy")
last_name = driver.find_element(By.ID, "billing_last_name")
last_name.send_keys("Zorin")

email = driver.find_element(By.ID, "billing_email")
email.send_keys("erw70r@gmail.com")

phone = driver.find_element(By.ID, "billing_phone")
phone.send_keys("89039039003")

country = driver.find_element(By.ID, "s2id_billing_country")
country.click()
country_search = driver.find_element(By.ID, "s2id_autogen1_search")
country_search.send_keys("Afghanistan")
country_select = driver.find_element(By.CLASS_NAME, "select2-match")
country_select.click()

address = driver.find_element(By.ID, "billing_address_1")
address.send_keys("Abbasova")

town = driver.find_element(By.ID, "billing_city")
town.send_keys("Kazan")

state = driver.find_element(By.ID, "billing_state")
state.send_keys("Tatarstan")

postcode = driver.find_element(By.ID, "billing_postcode")
postcode.send_keys("1234567890")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)

check_payments = driver.find_element(By.ID, "payment_method_cheque")
check_payments.click()
place_order_btn = driver.find_element(By.ID, "place_order")
place_order_btn.click()

thank_you = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))

payment_method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))





