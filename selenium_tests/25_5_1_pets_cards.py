import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    pytest.driver.implicitly_wait(10)
    pytest.driver.get("https://petfriends.skillfactory.ru/login")
    field_email = pytest.driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(valid_email)

    field_pass = pytest.driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)

    btn_submit = pytest.driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    yield

    pytest.driver.quit()


def test_pets_cards():
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
