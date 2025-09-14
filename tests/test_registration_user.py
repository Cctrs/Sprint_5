import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from datasets import *


class TestRegistration:

    def test_success_user_registration(self, driver, create_new_email):
        # Ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((element_card_is_located)))
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*login_and_registration_button).click()
        # Нажать кнопку «Нет аккаунта».
        driver.find_element(*no_account_button).click()
        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        driver.find_element(*email_input).send_keys(create_new_email)
        driver.find_element(*password_input).send_keys('parol123')
        driver.find_element(*password_confirm_input).send_keys('parol123')
        driver.find_element(*create_account_button).click()
        # Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((profile_name)))
        user_name = driver.find_element(*profile_name)
        # Получение пустой аватарки (тут зацепился за то, что не получилось разместить аватар и взял пустую картинку, 
        # в противном случае нужно будет учитывать какой-то более общий вариант проверки)
        user_avatar = driver.find_element(*profile_avatar).get_attribute('fill')

        assert user_name.text == 'User.'
        assert user_avatar == 'none'


    def test_exist_user_registration(self, driver):
        # Ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((element_card_is_located)))
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*login_and_registration_button).click()
        # Нажать кнопку «Нет аккаунта».
        driver.find_element(*no_account_button).click()
        # Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        driver.find_element(*email_input).send_keys(exist_user['email'])
        driver.find_element(*password_input).send_keys(exist_user['password'])
        driver.find_element(*password_confirm_input).send_keys(exist_user['password'])
        driver.find_element(*create_account_button).click()
        #Ожидание и ошибка
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((error_input)))
        border_color = driver.find_element(*error_input).value_of_css_property('border')
        error_text = driver.find_element(*error_input_text)

        assert "255, 105, 114" in border_color
        assert error_text.text == 'Ошибка'


    @pytest.mark.parametrize('emails', wrong_emails)
    def test_wrong_email_registration(self, driver, emails):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((element_card_is_located)))
        # Нажать кнопку «Вход и регистрация».
        driver.find_element(*login_and_registration_button).click()
        # Нажать кнопку «Нет аккаунта».
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((no_account_button)))
        # Переход на попап и ввод некорректного емейла
        driver.find_element(*no_account_button).click()
        driver.find_element(*email_input).send_keys(emails)
        driver.find_element(*create_account_button).click()
        # Найти и проверить выделение красным - стиль единый для всех полей ввода
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((error_input)))
        border_color = driver.find_element(*error_input).value_of_css_property('border')
        error_text = driver.find_element(*error_input_text)

        assert "255, 105, 114" in border_color
        assert error_text.text == 'Ошибка'