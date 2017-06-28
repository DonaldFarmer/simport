#!/usr/bin/env python
# -*- coding: latin-1 -*-
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ftplib import FTP
import paramiko
import zipfile
import sys
import os
# import pywinauto

"""

"""
isAbort = False
isLoggedin = False
isFtp = False
isReuse = False
isLogin = False
isCookies = False
isProducts = False
isLang = False

try:
  with open('config.json') as json_data_file:
    config = json.load(json_data_file)
except:
  print('No config.json found, use config.sample_json as a template')
  isAbort = True

for para in sys.argv:
  # print para
  if para.lower() == 'ftp':
    isFtp = True
  elif para.lower() == 'reuse':
    isReuse = True
  elif para.lower() == 'login':
    isLogin = True
  elif para.lower() == 'cookies':
    isCookies = True
  elif para.lower() == 'products':
    isProducts = True
  elif para.lower() == 'lang':
    isLang = True


def RetrieveFTPSFile(ftpdir, ftpfile, ftpsavefile):
  transport = paramiko.Transport((config['ftp_url'], config['ftp_port']))
  transport.connect(username = config['ftp_username'], password = config['ftp_password'])
  sftp = paramiko.SFTPClient.from_transport(transport)
  sftp.chdir(ftpdir)

  files = sftp.listdir()
  files.sort()
  files.reverse()

  cats = [elem for elem in files if 'catalog_20' in elem]
  langs = [elem for elem in files if 'french_' in elem]

  newest_cat = cats[-1]
  newest_lang = langs[-1]

  extension_cat = os.path.splitext(newest_cat)[1][1:].strip()
  if extension_cat.lower() == 'zip':
    print newest_cat, ' is a zip file', extension_cat

  extension_lang = os.path.splitext(newest_lang)[1][1:].strip()
  if extension_lang.lower() == 'zip':
    print newest_lang, ' is a zip file', extension_lang

  # ftpsourcefile = ftpdir + '/' + ftpfile
  # print ftpsourcefile
  # print newest
  localzipfile = 'ziptemp.zip'

  # sftp.get(ftpsourcefile, localzipfile)
  sftp.get(newest_cat, newest_cat)
  print 'Download catalog file completed. ', newest_cat
  sftp.get(newest_lang, newest_lang)
  print 'Download lang file completed. ', newest_cat

  sftp.close()
  transport.close()

  if extension_cat.lower() == 'zip':
    unzipper(newest_cat, ftpsavefile)
    print 'Unzip done.', ftpsavefile, ' created'

  if extension_lang.lower() == 'zip':
    unzipper(newest_lang, ftpsavefile)
    print 'Unzip done.', ftpsavefile, ' created'


def RetrieveFTPFile(ftpdir, ftpfile, ftpsavefile):
  ftp = FTP(config['ftp_url'])
  ftp.getwelcome()
  ftp.login(config['ftp_username'],config['ftp_password'])

  ftp.cwd(ftpdir)

  print('Files found on FTP site in directory', ftpdir)

  files = []
  try:
    files = ftp.nlst()
  except ftplib.error_perm, resp:
    if str(resp) == "550 No files found":
      print("No files in this directory.")
    else:
      raise 


  for f in files:
    print f
    extension = os.path.splitext(f)[1][1:].strip()
    print extension

    if extension.lower() == 'zip':
      print 'a zip file'
  

  ftpfilecmd = 'RETR ' + ftpfile
  print ftpfilecmd, ftpsavefile
  ftp.retrbinary(ftpfilecmd, open(ftpsavefile, 'wb').write)

  ftp.quit()

def unzipper(sourcefile, destfile):
  with zipfile.ZipFile(sourcefile,"r") as zip_ref:
    zip_ref.extractall(destfile)


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
  elif type == "linktxt":
    elem = driver.find_element_by_link_text(name)
  elif type == 'css':
    elem = driver.find_element_by_css_selector(name)
  try:
    elem.send_keys(val)
  except:
    print('unable to send keys {0} {1} {2}'.format(typ, name, val))



def clickandwait(): 
  pass


def click(driver, type, val):
  if type == "id":
    elem = driver.find_element_by_id(val) 
  elif type == "name":
    elem = driver.find_element_by_name(val) 
  elif type == "class":
    elem = driver.find_element_by_class_name(val)
  elif type == 'css':
    elem = driver.find_element_by_css_selector(val)
  elif type == "xpath":
    elem = driver.find_element_by_xpath(val) 
  elif type == "linktxt":
    elem = driver.find_element_by_link_text(val)
  elif type == "partial":
    elem = driver.find_element_by_partial_link_text(val) 

  try:
    elem.click()
  except:
    print('unable to click {0} {1}'.format(type, val))


def navigate(driver, val):
  driver.get(val)

def execute(driver, val):
  driver.execute_script(val)


def setCookiesFromFile(driver): # read the cookie from a file and set the session
  print 'Pulling cookie from file shopifyCookie.json'
  try:
    with open('shopifyCookie.json') as cjar:
      cookies = json.load(cjar)

      for cookie in cookies:
        driver.add_cookie(cookie)

      print json.dumps(cookies, indent=2)
      return True
      
  except:
    print('ran into a problem while reading shopifyCookie.json', sys.exc_info()[0])
    return

def saveCookiesToFile(): # write the session cookies to a file for later use
  print 'saving cookies to a shopifyCookie.json'
  cookies = driver.get_cookies()
  for cookie in cookies:
    if cookie['name']== 'EventPage_session':
      print 'EventPage_session', cookie['value']

  # print json.dumps(cookies, indent=2)
  with open('shopifyCookie.json', 'wb') as kjar:
    kjar.write(json.dumps(cookies))
    kjar.close


def saveSessionToFile():
  url = driver.command_executor._url
  session_id = driver.session_id
  print url, session_id
  sess = {}
  sess['url'] = url
  sess['session_id'] = session_id
  with open('session.json', 'wb') as file:
    file.write(json.dumps(sess))
    file.close()

def setSession():
  with open('session.json', 'rb') as file:
    sess = json.load(file)
    url = sess['url']
    session_id = sess['session_id']
    print url, session_id
    # try:
    # firefox_capabilities = DesiredCapabilities.FIREFOX
    # firefox_capabilities['marionette'] = True
    # capabilities=firefox_capabilities
    # browser = webdriver.Firefox(capabilities=firefox_capabilities)
    # print browser.service.port
    driver = webdriver.Remote(command_executor=url,desired_capabilities={})
    driver.session_id = session_id
    # except:
    #   print('ran into a problem while reusing session', sys.exc_info()[0])
    #   return
      
    driver.get(config['url_prod'])
    return true


# def Test(Name_of_File):
#     app = pywinauto.application.Application()
#     mainWindow = app[''] # main windows' title
#     ctrl=mainWindow['Edit'] 
#     mainWindow.SetFocus()
#     ctrl.ClickInput()
#     ctrl.TypeKeys(Name_of_File)
#     ctrlBis = mainWindow['Open'] # open file button
#     ctrlBis.ClickInput()

#############################################################################

if __name__ == "__main__" and  not isAbort:
  
  ### Open the Firefox browser and start a new session
  if  (isLang or isProducts):
    driver = init_driver()

  ### visit the FTP to see if we have files to process
  if isFtp:
    print 'Fetching data from FTP'
    RetrieveFTPSFile(config['ftp_dir_prod'], config['ftp_file_prod'], config['filepath_prod'])
  else:
    print 'skipping ftp, using local file ', config['filepath_prod']


  ### Visit the shopify login page
  if  (isLang or isProducts):
    openselenium(driver, config['url_prod'])
    WebDriverWait(driver, 5)

  ### replace session cookies from previous saved login session if requested
  if isLoggedin == False and isCookies:
    isLoggedin = setCookiesFromFile(driver)
    print cookies
    if cookies:
      for cookie in cookies:
        if cookie['name']== 'EventPage_session':
          driver.add_cookie(cookie)
      isLoggedin = True
    print 'isLoggedIn', isLoggedin
  # print 'current cookies'
  # print json.dumps(driver.get_cookies(), indent=1)

  ### Special Login that saves session cookies if requested
  if isLoggedin == False and isLogin:
    print 'need to login'
    print config['username']
    print config['password']
    type(driver, "id", "Content_ctl04_ctl00_txtUsername", config['username'])
    type(driver, "id", "Content_ctl04_ctl00_txtPassword", config['password'])
    click(driver, "id", "Content_ctl04_ctl00_btnLogin")
    WebDriverWait(driver, 5) 
    # print 'saving cookies'
    # saveCookiesToFile()
    print 'saving running session, do not close running tab'
    saveSessionToFile()
  else:
    print 'Skipping login'

  ### Connect to existing session if requested
  if isReuse:
    setSession()


  ### Normal shopify login if not logged in at this point
  if not isLoggedin and not isAbort and (isLang or isProducts):
    click(driver, "css", "button.login-form__link")
    WebDriverWait(driver, 50)
    if config['url_isproduction']:
      subdomain = "cma-joule-inc"
    else:
      subdomain = "sandbox-joule"
    type(driver, "id", "_subdomain", subdomain) #cma-joule-inc or sandbox-joule
    sleep(3)
    type(driver, "id", "_email", config['username'])
    sleep(3)
    type(driver, "id", "_password", config['password'])
    sleep(3)

    click(driver, "class", "marketing-button")
    sleep(3)
    # navigate(driver, 'https://sandbox-joule.myshopify.com/admin')
    # time.sleep(3)  

  if  (isLang or isProducts):
      main_window = driver.current_window_handle
  # import pdb; pdb.set_trace()


  ### Navigating to the product import page and get the product import popup

  if config['url_isproduction']:
    url_products = 'https://sandbox-joule.myshopify.com/admin/products'
  else:
    url_products = 'https://sandbox-joule.myshopify.com/admin/products'


  if isProducts and not isAbort:
    if config['url_isproduction']:
      url_products = 'https://sandbox-joule.myshopify.com/admin/products'
    else:
      url_products = 'https://sandbox-joule.myshopify.com/admin/products'

    navigate(driver, url_products)    ### Select the products import
    click(driver, "css", 'div.action-bar__top-links button+button')

    ### Requesting the import and specifying the file to use
    click(driver, "id", "overwrite_existing_products")
    type(driver, "id", "csv_input_field", config['filepath_prod'])
    click(driver, "id","upload-file-btn")
    WebDriverWait(driver, 50)



  if isLang and not isAbort:
    if config['url_isproduction']:
      url_lang = 'https://sandbox-joule.myshopify.com/admin/apps'
    else:
      url_lang = 'https://sandbox-joule.myshopify.com/admin/apps'

    navigate(driver, url_lang) 
    sleep(3)

    

    click(driver, "linktxt", "langify") # opens another tab
    sleep(3)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    driver.switch_to_window(main_window)
    sleep(2)

    navigate(driver, 'http://langify-app.com/') # ignore open tab but navigate with first tab
    sleep(3)
    
    
    # navigate(driver, 'http://langify-app.com/settings/language/edit/17818')
    
    # navigate(driver, 'http://langify-app.com/import/translations')
    # WebDriverWait(driver, 5)


    click(driver, 'css', 'ul.nav li a')
    sleep(1)
    click(driver, 'css', 'li.dropdown ul.dropdown-menu li+li+li a')

    # click(driver, "css", 'div.language-selection a')
    sleep(3)

    

    click(driver, "id", "import-intro-next")
    sleep(3)

    click(driver, "id", "import-step-1-next")
    sleep(3)

    click(driver, "id", "import-step-2-next")
    sleep(3)

    click(driver, "id", "import-step-3-next")
    sleep(3)

   
    import pdb; pdb.set_trace()

    click(driver, "id", "form_import_csv")
    sleep(3)

    type(driver, "id", "csv_input_field", config['filepath_lang'])
    click(driver, "id","upload-file-btn")

  #time.sleep(5)
  #driver.quit()