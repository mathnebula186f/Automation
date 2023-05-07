from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException

 
options=webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Edge(options=options)
driver.get("https://web.whatsapp.com/")
input("scan qr code")
while(1):
        # BuyandSell=driver.find_element(By.CSS_SELECTOR,'span[title="Buy&Sell Mess Coupons "]')
        FaltuGrpList = driver.find_elements(
            By.CSS_SELECTOR, 'div[class="lhggkp7q ln8gz9je rx9719la"]')#class means array of all chats
        for  grp in FaltuGrpList:
            if grp.find_elements(By.CSS_SELECTOR, 'span[title="Buy&Sell Mess Coupons "]') or grp.find_elements(By.CSS_SELECTOR, 'span[title="IIT Ropar CSE"]') or grp.find_elements(By.CSS_SELECTOR, 'span[title="Chenab EAST boiz"]'):
                try:
                    grp=grp.find_element(By.CSS_SELECTOR,'span[data-testid="icon-unread-count"]')
                    grp.click()
                except NoSuchElementException:
                    pass
                except ElementClickInterceptedException:
                    pass
        time.sleep(10)