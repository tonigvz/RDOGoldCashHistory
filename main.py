from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
import time
import re

PATH = "C:\Program Files (x86)\chromedriver.exe"
with open("D:\Projects\RDO\gc.txt", "r") as f:
    lines = f.read()
l = [i for i in lines.split()]
oldg = float(re.findall("\d+\.\d+", [i for i in l if i.startswith("gold")][-1])[0])
oldc = float(re.findall("\d+\.\d+", [i for i in l if i.startswith("cash")][-1])[0])


def get_gold_cash():

    driver = webdriver.Chrome(PATH)
    driver.get("https://socialclub.rockstargames.com/games/rdr2/catalogue/online/")
    sing_in = driver.find_element(By.LINK_TEXT, "Sign In")
    sing_in.click()
    time.sleep(5)
    username = driver.find_element(By.NAME, "email").send_keys("youremail")
    password = driver.find_element(By.NAME, "password").send_keys("yourpassword")
    time.sleep(5)
    sing_in2 = driver.find_element(
        By.XPATH,
        '//*[@id="app-page"]/div[2]/div[1]/div/div/form/fieldset[4]/div/button',
    ).click()
    driver.implicitly_wait(10)
    gold = driver.find_element(
        By.XPATH,
        '//*[@id="root"]/div[2]/header/div/div/div/div/div/a/span[2]',
    ).text
    cash = driver.find_element(
        By.CLASS_NAME, "Header__cashNumberAccessible__rteJ8"
    ).text
    new_line = "\n"
    gold_good = f"{gold[:3]}.{gold[3:5]}"
    gg = f"{date.today()}:{new_line}gold:{gold_good}{new_line}cash:{cash}{new_line}difference_cash:{float(gold_good)-oldg}{new_line}difference_gold:{float(cash)-oldc}"
    with open("D:\Projects\RDO\gc.txt", "r") as f:
        lines = f.read()
    if gold_good in lines and cash in lines:
        pass
    else:
        with open("D:\Projects\RDO\gc.txt", "a") as f:
            f.writelines(gg)


get_gold_cash()
