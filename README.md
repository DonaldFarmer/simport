# simport
Selenium command file to automate the importing of products into Shopify

Step 1 - Install Python 3.6.1 using Windows x86-64 Executable installer
https://www.python.org/downloads/release/python-361/


Step 2 - Download Pip installer script
https://bootstrap.pypa.io/get-pip.py


Step 3 - Move the get-pip.py file from the downloads directory to the c:\Python27 directory

Step 4 - Execute python command to install pip

```
c:\Python27> python get-pip.py
```
Step 5 - navigate to the scripts directory and run pip to install selenium

```
c:\Python27\scripts> pip install selenium
```
Step 6 - Download and run installer for Git
https://git-scm.com/download/win

Step 7 - Clone Git repo into c:\Python27 folder
```
cd c:\Python27
git clone https://github.com/DonaldFarmer/simport
cd c:\Python27\simport
```

Step 8 - (optional) Git command To get a newer copy of simport
```
c:\Python27\simport> Git pull origin master
```


h1 Instructions for Linux
Install python webdriver package
https://pypi.python.org/pypi/selenium

```python
sudo apt-get install python-pip

pip install selenium

cd ~/dev/cma

wget https://github.com/mozilla/geckodriver/releases/download/v0.16.0/geckodriver-v0.16.0-linux64.tar.gz

tar -xvzf geckodriver*

chmod +x geckodriver

sudo mv geckodriver /usr/bin
```

Instructions for Windows Users
http://selenium-python.readthedocs.io/installation.html#detailed-instructions-for-windows-users


Download latest chrome driver, unzip into development folder where the script is located
http://chromedriver.storage.googleapis.com/index.html


If you want to get the Selenium IDE
https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/

