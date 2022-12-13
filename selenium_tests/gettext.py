import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class GetText():
    def gettext(self):
        driver = webdriver.Chrome()
        driver.get("https://petfriends.skillfactory.ru/my_pets")
        time.sleep(3)
        text = driver.find_element(By.PARTIAL_LINK_TEXT, "Питомцев:")
        print(text)
        time.sleep(10)


findbytext = GetText()
findbytext.gettext()
