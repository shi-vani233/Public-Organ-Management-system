from django.test import TestCase

# Create your tests here.
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH ="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("http://127.0.0.1:8000/Hospital/loginpage/")
print(driver.title)
print("Login Test")
hos_email=driver.find_element_by_name("hospital_email")
hos_password=driver.find_element_by_name("password")

hos_submit=driver.find_element_by_id("volbtn")
hos_email.send_keys("dhyey@gmail.com")
hos_password.send_keys("shivanip")

hos_submit.send_keys(Keys.RETURN)