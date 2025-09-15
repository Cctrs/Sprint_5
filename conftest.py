import pytest
from selenium import webdriver
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def create_new_email():
    number = random.randint(101, 99999)
    new_email = f'test_mail{number}@gmail.com'
    return new_email