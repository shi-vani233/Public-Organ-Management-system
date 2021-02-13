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
driver.get("http://127.0.0.1:8000/Blood_Donation/Volunteer/")
print(driver.title)
print("all the volunteers having blood group A+")
search=driver.find_element_by_name("q")
search.send_keys("a+")
s=search.send_keys(Keys.RETURN)