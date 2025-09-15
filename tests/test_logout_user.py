from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datasets import exist_user
from locators import *


class TestLogOutUser:

    def test_logout_user(self, driver):
        # Ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(element_card_is_located))
        # Авторизация
        driver.find_element(*login_and_registration_button).click()
        driver.find_element(*email_input).send_keys(exist_user['email'])
        driver.find_element(*password_input).send_keys(exist_user['password'])
        driver.find_element(*login_button).click()
        # Ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(profile_name))
        # Выход из аккаунта
        driver.find_element(*logout_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(login_and_registration_button))
        # Поиск элементов после разлогина, имя и аватар не должны отображаться, кнопка логина должна
        user_name = driver.find_elements(*profile_name)
        user_avatar = driver.find_elements(*profile_avatar)
        find_login_button = driver.find_element(*login_and_registration_button)
        # Сравниваем пустые списки, возвращаемые через поиск элементов, если элемент не найден, то размер 0
        # Кнопка логина отображается
        assert len(user_name) == 0
        assert len(user_avatar) == 0
        assert find_login_button.is_displayed()