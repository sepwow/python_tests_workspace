import time
from selenium import webdriver

def test_search_example(selenium):

    driver = webdriver.Chrome()
    driver.get('https://google.com')

    time.sleep(3)

    search_input = selenium


