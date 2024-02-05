from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Giving the path of the chromedriver.exe
service = Service(executable_path="chromedriver.exe")
#Creating the driver object
driver = webdriver.Chrome(service=service)
#Opening the website
driver.get("http://google.com/")
#Finding the input element by class name
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
#Sending the search query to the input element
input_element.send_keys("Syed Danial Khurram" + Keys.ENTER)
#Finding the anchor element by xpath and clicking it
anchor_element = driver.find_element(By.XPATH, "//a[@href='https://pk.linkedin.com/in/syed-danial-khurram-a9982a205']")
anchor_element.click()
#Waiting for 5 seconds
time.sleep(5)
#Closing the browser
driver.quit()