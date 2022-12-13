import time
from config import email, password
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from gettext import GetText


def test_petfriends(driver):
    # Open PetFriends base page:
    driver = webdriver.Chrome()
    driver.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = driver.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = driver.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(email)

    # add password
    field_pass = driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(password)

    # click submit button
    btn_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
    if driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Make the screenshot of browser window:
        driver.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")

    # pytest -v --driver Chrome --driver-path /PycharmProjects/chromedriver.exe selenium_tests/test_selenium_petfriends.py