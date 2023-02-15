from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
path = "C:\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(4)
cook = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
cook.click()
lang = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
lang.click()
time.sleep(4)
cookie = driver.find_element(By.XPATH,'//*[@id="bigCookie"]')
n = True
while n:
    cookie.click()
    num = driver.find_element(By.XPATH, '//*[@id="productPrice0"]')
    num_cook = driver.find_element(By.XPATH, '//*[@id="cookies"]')
    m = driver.find_element(By.XPATH, '//*[@id="product0"]')
    num_cook_re = int(((num_cook.text).split())[0])
    if num_cook_re == int(num.get_attribute("innerHTML")):
        m.click()
c=input()