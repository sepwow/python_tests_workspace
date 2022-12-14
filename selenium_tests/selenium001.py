import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import valid_email, valid_password
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request


# @pytest.fixture(autouse=True)
# def testing():
#     pytest.driver = webdriver.Chrome()
#     pytest.driver.get("https://petfriends.skillfactory.ru/login")
#
#     yield
#
#     pytest.driver.quit()
# before usage "driver.__" change to "pytest.driver.__" everywhere


def test_pets_quantity(driver):
    driver = webdriver.Chrome()
    driver.get("https://petfriends.skillfactory.ru/login")

    time.sleep(3)

    field_email = driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    btn_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(3)

    driver.set_window_size(1920, 1080)

    # btn_hamburger = driver.find_element(By.CSS_SELECTOR, ".navbar-toggler.collapsed")
    # btn_hamburger.click()

    time.sleep(1)

    btn_my_pets = driver.find_element(By.CSS_SELECTOR, ".nav-link[href='/my_pets']")
    btn_my_pets.click()

    time.sleep(3)

    # tr_list = driver.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    # q_tr = len(tr_list)

    # text = urllib.request.urlopen('https://petfriends.skillfactory.ru/my_pets').read()
    # soup = BeautifulSoup(text)
    # tr_list = soup.select('.table.table-hover>tbody>tr')
    # q_tr = len(tr_list)

    tr_list = driver.find_elements(By.XPATH,
                                   '//*[@id="all_my_pets"]/table/tbody/tr')
    q_tr = str(len(tr_list))

    # sauce = urllib.request.urlopen('https://petfriends.skillfactory.ru/my_pets').read()
    # soup = bs.BeautifulSoup(sauce, 'lxml')
    #
    # table = soup.find('tbody')
    # tr_list = table.find_all('tr')
    # q_tr = len(tr_list)

    pets_numb = driver.find_element(By.XPATH,
                                    '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(": ")[1]

        # in general this trick should have done right:
    # tr_list = driver.find_element(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # q_tr = str(len(tr_list))

    # tr_list = driver.find_element(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    # q_tr = str(len(tr_list))

    # tr_list = driver.find_element(By.XPATH, '//table[@class=\"table.table-hover\"]/tbody/tr')
    # q_tr = str(len(tr_list))

    # tr_list = lxml.html.fragment_fromstring(html, create_parent = True)
    # tr_list.xpath('count(table[@class="table.table-hover"]/tbody/tr)')

    # text = driver.find_element(By.PARTIAL_LINK_TEXT, "????????????????:")
    # print(text)
    # time.sleep(5)

    # findbytext = GetText()
    # text = findbytext.gettext()

    # assert text[:-1:] == q_tr
    assert pets_numb == q_tr

    # pytest -v --driver Chrome --driver-path /PycharmProjects/chromedriver.exe selenium_tests/selenium001.py



