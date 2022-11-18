#first you need to install selenium library
#pip install selenium

from selenium import webdriver
import time
    
x = input("Enter the URL ")
refreshrate = input("Enter the number of seconds ")
refreshrate = int(refreshrate)
# optional: if you don't need to open the browser just add the two lines below 
#op = webdriver.ChromeOptions()
#op.add_argument('headless')
driver = webdriver.Chrome() # and replace this line by driver = webdriver.Chrome(options=op)
driver.get(x)

while True:
    time.sleep(refreshrate)
    driver.refresh()