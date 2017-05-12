#!/usr/bin/env python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
import a new product csv file
init driver
configure
login
navigate to import page
"""
 
url = ""
username = ""
password = ""
filepath = ""


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def checkfile(): # check and see if a valid file exists at upload location
  pass

def open(driver, uri): # navigates to webpage
  driver.get(uri)

def type(driver, type, name, value):
  if type == "id":
    elem = driver.find_element_by_id(name) 

  try:
    elem.send_keys(value)
  except:
    print('unable to send keys {0} {1} {2}'.format(type, name, value))

def clickandwait(): 
  pass

def click(driver, type, value)
  if type = "id":
    elem = driver.find_element_by_id(value) 
  elif type == "name":
    elem = driver.find_element_by_name(value) 
  elif type == "xpath":
    elem = driver.find_element_by_xpath(value) 

  try:
    elem.click()
  except ElementNotVisibleException:
    print('unable to click {0} {1}'.format(type, value))


 
if __name__ == "__main__":
  driver = init_driver()

  open(driver, "https://sandbox-joule.myshopify.com/admin/auth/login")
  type(driver, "id", "login-input", "don.farmer@cma.ca")
  type(driver, "id", "password", "")
  click(driver, "name", "commit")
  click(driver, "xpath","//div[@id='NextNavigation']/div/nav/ol/li[3]/a/span")
  click(driver, "id", "ui-popover-activator--2")
  click(driver, "xpath", "(//button[@name='button'])[7]")
  type(driver, "id", "csv_input_field", "/home/donald/Documents/product_template.csv")
  click(driver, "id","upload-file-btn")


  open(driver, "https://sandbox-joule.myshopify.com/admin/apps")
  click(driver, "link", "langify")
  click(driver, "link", "Français")
  clickandwait(driver, "link", "Import translations...")
  click(driver, "link", "import-intro-next")
  click(driver, "link", "form_themes_0")
  click(driver, "link", "import-step-1-next")
  click(driver, "link", "form_categories_0")
  click(driver, "link", "form_categories_2")
  click(driver, "link", "form_categories_3")
  click(driver, "link", "form_categories_4")
  click(driver, "link", "form_categories_5")
  click(driver, "link", "import-step-2-next")
  click(driver, "link", "import-step-3-next")
  click(driver, "link", "form_import_csv")
  #type(driver, "id", "csv_input_field", "/home/donald/Documents/lang.csv")
  #click(driver, "id","upload-file-btn")

  #time.sleep(5)
  #driver.quit()