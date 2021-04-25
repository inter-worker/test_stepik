from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os 

def calc(x):
        return math.log(abs(12*math.sin(x)))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector(".trollface.btn").click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    text1 = int(browser.find_element_by_id("input_value").text)
    y = str(calc(text1))
    input2 = browser.find_element_by_id("answer").send_keys(y)
    input3 = browser.find_element_by_css_selector("button.btn").click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()