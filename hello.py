import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/olgaserebrennikova/Desktop/Hello/chromedriver')
driver.get("https://test.integration.i.alacartewheel.com/")
driver.implicitly_wait(10)
login=driver.find_element_by_css_selector('button.au-target.button-primary').click()
driver.switch_to_window(driver.window_handles[1])
email=driver.find_element_by_css_selector('input[id="Username"]').send_keys('admin@example.com')
password=driver.find_element_by_css_selector('input[id="Password"]').send_keys('tulle76"Mule')
loginbutton=driver.find_element_by_id('login-button').click()


