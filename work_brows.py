import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def to_file(list):
    try:
        file = open('users.txt', 'w')
    except Exception:
        print("Ой ой.... Что-то с файлом")
        return

    for num in range(len(list)):
        file.writelines(str(num+1)+". " + str(list[num]) + '\n')
    file.close()


def log_in(driver):
    driver.get("https://www.facebook.com/")
    login = "+380665007351"
    password = "01052001Egorwot"

    login_element = driver.find_element_by_name("email")
    password_element = driver.find_element_by_name("pass")
    enter_element = driver.find_element_by_name("login")

    login_element.send_keys(login)
    password_element.send_keys(password)
    enter_element.click()

def get_link(driver):
    list_link = []
    for i in range(10):
        list_friend = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/ html / body / div[1] / div / div[1] / div / div[3] / div / div / div[1] / div[1] / div / div[3] / div / div / div[1] / div / div[2] / div / div[2] / div / ul")))

        friends = list_friend.find_elements_by_tag_name("li")

        friends[i].click()

        cross = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[3]/span[4]/div")))

        upper_left = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/span/div/div[1]")))
        upper_left.click()

        button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/a[2]")))

        list_link.append(button.get_attribute("href"))
        cross.click()

    to_file(list_link)
    driver.close()

def main():
    s = Service('./geckodriver')
    driver = webdriver.Firefox(service=s)
    log_in(driver)
    get_link(driver)


if __name__ == '__main__':
    main()



