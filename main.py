from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"


def get_gold_cash():
    driver = webdriver.Chrome(PATH)
    driver.get("https://socialclub.rockstargames.com/games/rdr2/catalogue/online/")
    sing_in = driver.find_element(By.LINK_TEXT, "Sign In")
    sing_in.click()
    time.sleep(5)
    username = driver.find_element(By.NAME, "email").send_keys("###")
    password = driver.find_element(By.NAME, "password").send_keys("###")
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
    gg = f"{new_line}{date.today()}:{new_line}gold:{gold_good}{new_line}cash:{cash}"
    with open("new.txt", "r") as f:
        lines = f.read()
    if gold_good in lines and cash in lines:
        pass
    else:
        with open("new.txt", "a") as f:
            f.writelines(gg)


get_gold_cash()
