from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datasets import exist_user
from locators import *


class TestAuthorization:

    def test_login_success(self, driver):
        # Ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((element_card_is_located)))
        # Переход по кнопке авторизации и ввод всех данных существующего аккаунта
        driver.find_element(*login_and_registration_button).click()
        driver.find_element(*email_input).send_keys(exist_user['email'])
        driver.find_element(*password_input).send_keys(exist_user['password'])
        driver.find_element(*login_button).click()
        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((profile_name)))
        user_name = driver.find_element(*profile_name)
        # Получение пустой аватарки (тут зацепился за то, что не получилось разместить аватар и взял пустую картинку, 
        # в противном случае нужно будет учитывать какой-то более общий вариант проверки)
        user_avatar = driver.find_element(*profile_avatar).get_attribute('fill')

        assert user_name.text == 'User.'
        assert user_avatar == 'none'