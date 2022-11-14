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

ID=1
while True:

    
    laptop_thumbnails=page.find_elements(By.CLASS_NAME,"title")
 
    for thumbnail in laptop_thumbnails:
        time.sleep(3)
        thumbnail.click()
        Name=page.find_element(By.XPATH,"//h4")
        Price=page.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]")
        Specifications=page.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p")
        Number_Of_Reviews=page.find_element(By.XPATH,"//p")
        page.back()
        split_text=page.text.split(" ")
        writer.writerow([ID,Name.text,Price.text,Specifications.text,Number_Of_Reviews.text])
        ID += 1

    try:
        element=page.find_element(By.PARTIAL_LINK_TEXT,"›")
        element.click()
    except NoSuchElementException:
        break    

# ›






file.close()
page.quit()




