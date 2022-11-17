from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv
import time
import pandas as pandasforsortingcsv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


file=open("laptops.csv","w",newline="")
writer=csv.writer(file)
writer.writerow(["ID","Name","Price","Specifications","Number of Reviews"])

browser_driver=Service("./chromedriver.exe")
page=webdriver.Chrome(service=browser_driver)
page.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")
cookies=WebDriverWait(page,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"acceptCookies")))
cookies.click()


ID=0
while True:
    laptop_thumbnails=page.find_elements(By.CLASS_NAME,"title")
    for thumbnail in laptop_thumbnails:
        thumbnail.click()
        time.sleep(1)
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




csv_data=pandasforsortingcsv.read_csv("laptops.csv")
csv_data.sort_values(["Price"],axis=0,ascending=[False],inplace=True)


file.close()
page.quit()




