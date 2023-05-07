from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException , WebDriverException ,StaleElementReferenceException
from selenium.webdriver.common import action_chains



options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
actions = action_chains.ActionChains(driver)
driver.get("https://www.instagram.com/direct/inbox/")
input("Log in")
# time.sleep(3)
# # messageSymbol = driver.find_element(
# #     By.CSS_SELECTOR, 'div[class="x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv"]')
# # messageSymbol.click()
# time.sleep(5)
while (1):
        driver.switch_to.default_content()
            # BuyandSell=driver.find_element(By.CSS_SELECTOR,'span[title="Buy&Sell Mess Coupons "]')
        try:
            FaltuGrpList = driver.find_elements(
                By.CSS_SELECTOR, 'div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xc73u3c x5ib6vp xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]')  # class means array of all chats
            for grp in FaltuGrpList:
                if grp.find_elements(By.CSS_SELECTOR, 'div[aria-label="Unread"]'):
                        grp = grp.find_element(
                            By.CSS_SELECTOR, 'span[class="_aacl _aaco _aacw _aacx _aad7"]')
                        MessageText=grp.text
                        if(MessageText[0:4]=="Sent" or MessageText[0:7]=="Reacted" or MessageText[0:5]=="Liked"):
                            try:
                                grp.click()
                                time.sleep(2)
                                MessageArray = driver.find_elements(
                                    By.CSS_SELECTOR, 'div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv xuk3077 x1oa3qoh x1nhvcw1"]')
                                
                                time.sleep(2)
                                print("length of array=",len(MessageArray))
                                latestMessage=MessageArray[len(MessageArray)-1]
                                time.sleep(3)
                                actions.double_click(latestMessage).perform()
                            except StaleElementReferenceException:
                                pass
                            except NoSuchElementException:
                                pass
                            except ElementClickInterceptedException:
                                pass
                            except WebDriverException:
                                pass
                            driver.switch_to.default_content()
        except StaleElementReferenceException:
            pass
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            pass
        except WebDriverException:
            pass
        time.sleep(10)
    