from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from datasets import exist_user


class TestCreateItem:

    def test_create_item_authorized(self, driver):
        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((element_card_is_located)))
        # Вход под существующим юзером
        driver.find_element(*login_and_registration_button).click()
        driver.find_element(*email_input).send_keys(exist_user['email'])
        driver.find_element(*password_input).send_keys(exist_user['password'])
        driver.find_element(*login_button).click()
        # Ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((profile_name)))
        # Кнопка создания объявления
        driver.find_element(*create_item_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((item_name_input)))
        # Заполнение карточки товара
        driver.find_element(*item_name_input).send_keys('Гараж')
        driver.find_element(*item_description_input).send_keys('Продам гараж')
        driver.find_element(*item_price_input).send_keys(10000)
        # Выбор и заполнение категории товара
        driver.find_elements(*dropdown_menu)[0].click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((dropdown_category_selected)))
        driver.find_element(*dropdown_category_selected).click()
        # Выбор и заполнение города товара
        driver.find_elements(*dropdown_menu)[1].click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((dropdown_city_selected)))
        driver.find_element(*dropdown_city_selected).click()
        # Создание объявления
        driver.find_element(*share_item_button).click()
        # Ожидание прогрузки после создания
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((element_card_is_located)))
        # Переход в профиль
        driver.find_element(*profile_avatar_button).click()
        # Ожидание загрузки профиля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((element_card_is_located)))
        # Поиск созданного айтема и сравнение, что это именно он
        created_item = driver.find_element(*created_item_text)
        assert created_item.text == 'Гараж'


    def test_create_item_unauthorized(self, driver):
        # Ожидание
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((element_card_is_located)))
        # Кнопка размещения объявления
        driver.find_element(*create_item_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((popup_auth_before_create_item)))
        # Появление попапа об авторизации
        popup_text = driver.find_element(*popup_auth_before_create_item_text)

        assert popup_text.text == 'Чтобы разместить объявление, авторизуйтесь'