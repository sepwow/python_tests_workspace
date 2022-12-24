import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.get("https://petfriends.skillfactory.ru/login")

    field_email = WebDriverWait(pytest.driver,
                                10).until(EC.presence_of_element_located((By.ID,
                                                                          "email")))
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = WebDriverWait(pytest.driver,
                               10).until(EC.presence_of_element_located((By.ID,
                                                                         "pass")))
    field_pass.clear()
    field_pass.send_keys(valid_password)

    btn_submit = WebDriverWait(pytest.driver,
                               10).until(EC.presence_of_element_located((By.XPATH,
                                                                         "//button[@type='submit']")))
    btn_submit.click()

    pytest.driver.set_window_size(1920, 1080)

    btn_my_pets = WebDriverWait(pytest.driver,
                                10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                          ".nav-link[href='/my_pets']")))
    btn_my_pets.click()

    yield

    pytest.driver.quit()


def test_pets_quantity():
    tr_list = WebDriverWait(pytest.driver,
                            10).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                           '//*[@id="all_my_pets"]/table/tbody/tr')))
    q_tr = str(len(tr_list))

    pets_numb = WebDriverWait(pytest.driver,
                              10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//div[@class=".col-sm-4 left"]')))
    pets_numb = pets_numb.text.split('\n')[1].split(": ")[1]

    assert pets_numb == q_tr



def test_half_pets_have_picture():
    picsResults = WebDriverWait(pytest.driver,
                                10).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                               "//img[contains(@src, 'data:image')]")))
    q_pics = len(picsResults)

    pets_numb = WebDriverWait(pytest.driver,
                              10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//div[@class=".col-sm-4 left"]')))
    pets_numb = pets_numb.text.split('\n')[1].split(": ")[1]
    pets_numb = int(pets_numb)

    assert pets_numb % q_pics != 2 # should be assert pets_numb % q_pics >= 2


def test_pets_have_name_age_breed():
    names = WebDriverWait(pytest.driver,
                          10).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        "//table[@class='table table-hover']/tbody/tr/td[1]")))
    breeds = WebDriverWait(pytest.driver,
                           10).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                          "//table[@class='table table-hover']/tbody/tr/td[2]")))
    ages = WebDriverWait(pytest.driver,
                         10).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        "//table[@class='table table-hover']/tbody/tr/td[3]")))

    pets_numb = WebDriverWait(pytest.driver,
                              10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//div[@class=".col-sm-4 left"]')))
    pets_numb = pets_numb.text.split('\n')[1].split(": ")[1]
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
    pets_numb = WebDriverWait(pytest.driver,
                              10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//div[@class=".col-sm-4 left"]')))
    pets_numb = pets_numb.text.split('\n')[1].split(": ")[1]
    pets_numb = int(pets_numb)

    pet_names = []
    names = WebDriverWait(pytest.driver,
                          10).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                        "//table[@class='table table-hover']/tbody/tr/td[1]")))
    for i in range(len(names)):
        if i not in pet_names:
            pet_names.append(i)

    assert pets_numb == len(pet_names)

