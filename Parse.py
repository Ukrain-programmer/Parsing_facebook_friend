import time
import getpass
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Constants import *

def to_file(list):
    name = 0
    link_user = 1
    try:
        file = open(FILE_NAME, 'w')
    except Exception:
        print("Ой ой.... Что-то с файлом")
        return

    for num in range(len(list)):
        file.writelines(str(list[num][name])+":  " + str(list[num][link_user]) + '\n')
    file.close()

def log_in(driver, password):

    driver.get(SITE_UML)
    login = LOGIN



    login_element = driver.find_element_by_name("email")
    password_element = driver.find_element_by_name("pass")
    enter_element = driver.find_element_by_name("login")

    login_element.send_keys(login)
    password_element.send_keys(password)
    enter_element.click()


def go_to(driver, xpath):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )).click()

def to_friends(driver):
    go_to(driver, PROFILE_XPATH)
    time.sleep(3)
    go_to(driver, FRIEND_XPATH)

def get_friend_list(driver):
    parsed_list = []
    count = 0
    while True:
        try:
            element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, START_FRIEND_XPATH.format(count+1))))
            friend = element.find_element_by_xpath('.//div[2]/div[1]/a/span').get_attribute('innerText')
            link = element.find_element_by_xpath('.//div[2]/div[1]/a').get_attribute('href')
            parsed_list.append([friend, link])
            count+=1
        except:
            to_file(parsed_list)
            print("users - " + str(count-1))
            return



def scroll_page(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(3)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def main():
    password = getpass.getpass()
    s = Service('./geckodriver')
    driver = webdriver.Firefox(service=s)
    driver.maximize_window()
    log_in(driver, password)
    to_friends(driver)
    scroll_page(driver)
    get_friend_list(driver)
    driver.close()



if __name__ == '__main__':
    main()