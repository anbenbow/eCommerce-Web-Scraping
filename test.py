from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv
import time

file=open("laptops.csv","w",newline="")
writer=csv.writer(file)
writer.writerow(["ID","Name","Price","Specifications","Number of Reviews"])

browser_driver=Service("./chromedriver.exe")
page=webdriver.Chrome(service=browser_driver)
page.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

ID=0
while True:
    laptop_thumbnails=page.find_elements(By.CLASS_NAME,"title")
    for thumbnail in laptop_thumbnails:
        thumbnail.click()
        time.sleep(3)
        Name=page.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]").text
        Price=page.find_element(By.XPATH,"//h4").text
        Specifications=page.find_element(By.CLASS_NAME,"description").text
        Number_Of_Reviews=page.find_element(By.CLASS_NAME,"ratings").text
        ID += 1
        writer.writerow([ID,Name,Price,Specifications,Number_Of_Reviews])
        
        page.back()
    try:
        #element=page.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/ul/li[13]/a")
        element=page.find_element(By.PARTIAL_LINK_TEXT,"›")
        element.click()
    except NoSuchElementException:
        break    



    file.close()
    page.quit()