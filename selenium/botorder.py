import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    PATH = "C:\Program Files (x86)\chromedriver.exe" #setting path for the Chrome driver controller
    driver = webdriver.Chrome(PATH) 
    #driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
    driver.get("https://www.bestbuy.com/site/marvels-spider-man-miles-morales-ultimate-launch-edition-playstation-5/6430159.p?skuId=6430159")
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[6]/div[1]/div/div/div/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button').click()
    time.sleep(5)
    input_email = driver.find_element_by_id('user.emailAddress')
    input_email.send_keys('chadsrealvoice@gmail.com')
    input_phone = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input')
    input_phone.send_keys('9549891827')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button').click()
    time.sleep(5)
    input_CC = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[1]/div/input')
    input_CC.send_keys('4440039482847294')
    input_CCMonth = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[1]/div/div[1]/label/div/div/select')
    print(input_CCMonth)  

myFirstName = 'John'
myLastName = 'Smith'
myEmail = 'mail@gmail.com'
myAddress = '1234 Apple Lane'
myPhone = '1234567890'
myCreditCardNum = '123456789'
myCreditExpireMonth = '00'
myCreditExpireYear = '25'
myCVV = '123'
