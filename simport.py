#!/usr/bin/env python
# -*- coding: latin-1 -*-
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
isAbort = False
try:
  with open('config.json') as json_data_file:
    config = json.load(json_data_file)
except:
  print('no config.json found, use config.sample_json as a template')
  isAbort = True


# url_prod = "https://sandbox-joule.myshopify.com/admin/products"
# url_lang = "https://sandbox-joule.myshopify.com/admin/apps"
# username = "don.farmer@cma.ca"
# password = ""
# filepath_prod = "/home/donald/Documents/product_template.csv"
# filepath_lang = "/home/donald/Documents/lang.csv"

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def checkfile(): # check and see if a valid file exists at upload location
  pass


def openselenium(driver, uri): # navigates to webpage
  driver.get(uri)


def type(driver, typ, name, val):
  if typ == "id":
    elem = driver.find_element_by_id(name) 
  elif typ == "class":
    elem = driver.find_element_by_class_name(name)
  try:
    elem.send_keys(val)
  except:
    print('unable to send keys {0} {1} {2}'.format(typ, name, val))



def clickandwait(): 
  pass


def click(driver, type, value):
  if type == "id":
    elem = driver.find_element_by_id(value) 
  elif type == "name":
    elem = driver.find_element_by_name(value) 
  elif type == "xpath":
    elem = driver.find_element_by_xpath(value) 
  elif type == "linktxt":
    elem = driver.find_element_by_link_text(value)
  try:
    elem.click()
  except:
    print('unable to click {0} {1}'.format(type, value))


def navigate(driver, val):
  driver.url(val)


if __name__ == "__main__" and  not isAbort:
  driver = init_driver()
  print(config['username'])
  # openselenium(driver, url_prod)
  # WebDriverWait(driver, 5)


  # type(driver, "id", "login-input", config['username'])
  # type(driver, "id", config['password'], "")
  # type(driver, "class", "dialog-btn", Keys.RETURN)
  # WebDriverWait(driver, 3)

  # navigate(driver, "https://sandbox-joule.myshopify.com/admin/products") # s/b on this page now

  # click(driver, "linktext","Products")
  # WebDriverWait(driver, 2)
  # click(driver, "linktext", "Import")

  # click(driver, "id", "overwrite_existing_products")
  # type(driver, "id", "csv_input_field", config['filepath_prod'])
  # click(driver, "id","upload-file-btn")


  # need to wait until previous upload is finished
  # navigate(driver, config['url_lang']) 
  # click(driver, "link", "langify")
  # click(driver, "link", "Français")
  # clickandwait(driver, "link", "Import translations...")
  # click(driver, "link", "import-intro-next")
  # click(driver, "link", "form_themes_0")
  # click(driver, "link", "import-step-1-next")
  # click(driver, "link", "form_categories_0")
  # click(driver, "link", "form_categories_2")
  # click(driver, "link", "form_categories_3")
  # click(driver, "link", "form_categories_4")
  # click(driver, "link", "form_categories_5")
  # click(driver, "link", "import-step-2-next")
  # click(driver, "link", "import-step-3-next")
  # click(driver, "link", "form_import_csv")
  # #type(driver, "id", "csv_input_field", config['filepath_lang'])
  # #click(driver, "id","upload-file-btn")

  #time.sleep(5)
  #driver.quit()