import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def timer():
    start_time = time.time()
    time.sleep(20)
    end_time = time.time()
    print(end_time)


driver = webdriver.Firefox()
driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
fullButton = driver.find_element(By.CLASS_NAME, "ytp-fullscreen-button.ytp-button")
fullButton.send_keys(Keys.RETURN)
timer()
driver.close()
