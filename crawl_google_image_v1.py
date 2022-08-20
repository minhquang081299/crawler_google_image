from selenium import webdriver
import selenium
import time
from selenium.webdriver.support.ui import Select
import cv2 as cv 
import shutil
import sys
import tkinter as tk
from tkinter import filedialog

import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def crawler_image(begin_url,new_dir):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    chrpath = os.getcwd().replace("\\", "//")
    driver = webdriver.Chrome(chrpath+'/chromedriver.exe')
    import urllib.request
    checkpoint = 0

    # print('Input:')
    # new_dir = 'ok'
    if (os.path.exists(f"data/{new_dir}")):
        folder_path = f"data/{new_dir}"
        print('ok')
    else:

        folder_path = f"data/{new_dir}"
        os.mkdir(folder_path)
    while(True):
        # begin_url=url_p
        # begin_url = 'https://www.google.com/search?q=d%C3%A1nh+nhau&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjcoYXos7b5AhVW82EKHZ39BhEQ_AUoAXoECAEQAw&biw=1846&bih=952&dpr=1'
        list_url = []
        driver.get(begin_url)
        # time.sleep(5)
        times = 0
        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(SCROLL_PAUSE_TIME)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            times+=1
            # time.sleep(3)
            if times == 20: 
                break
            try:
                driver.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[2]/div[2]/input').click()
                # /html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img
                # time.sleep(2)
            except:
                continue

        #return top
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
        for i in range(checkpoint, 500):
            if driver.current_url != begin_url:
                # print(driver.current_url)

                checkpoint = i+1
                begin_url==driver.current_url
                print(i)
                break
            else:
                pass
            
            try:
                driver.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div['+str(i+1)+']').click()
            except:
                continue
            
            try:
                time.sleep(1.5)
                url = driver.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div').find_element(By.TAG_NAME,'img').get_attribute("src")
            except:
                continue
            try:
                urllib.request.urlretrieve(url,f"data/{new_dir}/{new_dir}"+'_'+ str(i)+".jpg")
            except:
                continue
            # time.sleep(3)
            driver.find_element(By.CLASS_NAME,'hm60ue').click()
            # time.sleep(3)
            print("ok"+str(i))
            if i == 500:
                checkpoint == i
        if checkpoint == 500:
            break
# crawler_image('Đánh Nhau')