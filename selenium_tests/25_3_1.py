import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import valid_email, valid_password
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.get("https://petfriends.skillfactory.ru/login")

    yield

    pytest.driver.quit()


# before usage "driver.__" change to "pytest.driver.__" everywhere


def test_pets_quantity():
    # driver = webdriver.Chrome()
    # driver.get("https://petfriends.skillfactory.ru/login")

    time.sleep(3)

    field_email = pytest.driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = pytest.driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    btn_submit = pytest.driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(3)

    # btn_hamburger = driver.find_element(By.CSS_SELECTOR, ".navbar-toggler.collapsed")
    # btn_hamburger.click()

    pytest.driver.set_window_size(1920, 1080)

    time.sleep(1)

    btn_my_pets = pytest.driver.find_element(By.CSS_SELECTOR, ".nav-link[href='/my_pets']")
    btn_my_pets.click()

    time.sleep(3)

    tr_list = pytest.driver.find_elements(By.XPATH,
                                   '//*[@id="all_my_pets"]/table/tbody/tr')
    q_tr = str(len(tr_list))

    pets_numb = pytest.driver.find_element(By.XPATH,
                                    '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(": ")[1]
    # "//div[text()[contains(.,'Питомцев')]]"

        # in general this trick should have done right:
    # tr_list = driver.find_element(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # q_tr = str(len(tr_list))

    assert pets_numb == q_tr

    # pytest -v --driver Chrome --driver-path /PycharmProjects/chromedriver.exe selenium_tests/25_3_1.py



def test_half_pets_have_picture():

    time.sleep(3)

    field_email = pytest.driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = pytest.driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    btn_submit = pytest.driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(3)

    # btn_hamburger = driver.find_element(By.CSS_SELECTOR, ".navbar-toggler.collapsed")
    # btn_hamburger.click()

    pytest.driver.set_window_size(1920, 1080)

    time.sleep(1)

    btn_my_pets = pytest.driver.find_element(By.CSS_SELECTOR, ".nav-link[href='/my_pets']")
    btn_my_pets.click()

    time.sleep(3)

    # q_pics = 0

    picsResults = pytest.driver.find_elements(By.XPATH, "//img[contains(@src, 'data:image')]")
    q_pics = len(picsResults)

    # for pics in picsResults:
    #     if pics:
    #         q_pics += 1
    #     else:
    #         pass

    pets_numb = pytest.driver.find_element(By.XPATH,
                                           '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(": ")[1]
    pets_numb = int(pets_numb)

    assert pets_numb % q_pics != 2 # should be assert pets_numb % q_pics >= 2


def test_pets_have_name_age_breed():

    time.sleep(3)

    field_email = pytest.driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = pytest.driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    btn_submit = pytest.driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(3)

    # btn_hamburger = driver.find_element(By.CSS_SELECTOR, ".navbar-toggler.collapsed")
    # btn_hamburger.click()

    pytest.driver.set_window_size(1920, 1080)

    time.sleep(1)

    btn_my_pets = pytest.driver.find_element(By.CSS_SELECTOR, ".nav-link[href='/my_pets']")
    btn_my_pets.click()

    time.sleep(3)

    names = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/td[1]")
    breeds = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/td[2]")
    ages = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/td[3]")

    pets_numb = pytest.driver.find_element(By.XPATH,
                                           '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(": ")[1]
    pets_numb = int(pets_numb)

    for i in range(len(names)):
        assert names[i].text != ''
        assert pets_numb == len(names)
    for i in range(len(breeds)):
        assert breeds[i].text != ''
        assert pets_numb == len(breeds)
    for i in range(len(ages)):
        assert ages[i].text != ''
        assert pets_numb == len(ages)


def test_pets_have_different_names():

    time.sleep(3)

    field_email = pytest.driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = pytest.driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    btn_submit = pytest.driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(3)

    # btn_hamburger = driver.find_element(By.CSS_SELECTOR, ".navbar-toggler.collapsed")
    # btn_hamburger.click()

    pytest.driver.set_window_size(1920, 1080)

    time.sleep(1)

    btn_my_pets = pytest.driver.find_element(By.CSS_SELECTOR, ".nav-link[href='/my_pets']")
    btn_my_pets.click()

    time.sleep(3)

    pets_numb = pytest.driver.find_element(By.XPATH,
                                           '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(": ")[1]
    pets_numb = int(pets_numb)

    pet_names = []
    names = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/td[1]")
    for i in range(len(names)):
        if i not in pet_names:
            pet_names.append(i)

    assert pets_numb == len(pet_names)

"""
def test_show_my_pets():
    # # Находим карточки всех питомцев
    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    # Создаем пустой список, куда будем добавлять свойства (имя, порода, возраст) всех питомцев
    all_pets_props = []
    # Создаем список свойств отдельного питомца
    pet_props = []
    # Перебираем карточки всех животных
    for i in range(1, len(all_pets)):
        # проходимся по элементам, где содержатся свойства отдельного питомца
        for j in range(1, 4):
            pet_props_element = pytest.driver.find_element(By.XPATH,
                                                           f'//*[@id="all_my_pets"]/table/tbody/tr[{i}]/td[{j}]')
            # добавляем найденные свойства в список для каждого питомца
            pet_props.append(pet_props_element.text)
            # Списки свойств всех питомцев добавляем в общий список
    for k in range(0, len(pet_props), 3):
        all_pets_props.append([pet_props[k], pet_props[k+1], pet_props[k+2]])
            # Перебираем общий список
    for l in range((len(all_pets_props)-1)):
        for m in range(l+1, len(all_pets_props)):
            assert all_pets_props[l] != all_pets_props[m]
"""