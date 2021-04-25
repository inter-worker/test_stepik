from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os 

def calc(x):
        return math.log(abs(12*math.sin(x)))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    #browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(2)
    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    #selenium.webdriver.support.expected_conditions.text_to_be_present_in_element( локатор , текст_ )
    butt = browser.find_element_by_id("book").click()
    
    text1 = int(browser.find_element_by_id("input_value").text)
    y = str(calc(text1))
    input2 = browser.find_element_by_id("answer").send_keys(y)
    input3 = browser.find_element_by_id("solve").click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()