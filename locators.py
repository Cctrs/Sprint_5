from selenium.webdriver.common.by import By

# Кнопки
login_and_registration_button = (By.XPATH, ".//button[text()='Вход и регистрация']")
no_account_button = (By.XPATH, ".//button[text()='Нет аккаунта']")
create_account_button = (By.XPATH, ".//button[text()='Создать аккаунт']")
login_button = (By.XPATH, ".//button[text()='Войти']")
create_item_button = (By.XPATH, ".//button[text()='Разместить объявление']")
share_item_button = (By.XPATH, ".//button[text()='Опубликовать']")
logout_button = (By.XPATH, ".//button[text()='Выйти']")

# Поля формы авторизации
email_input = (By.NAME, "email")
password_input = (By.NAME, "password")
password_confirm_input = (By.NAME, "submitPassword")

# Поля формы объявления
item_name_input = (By.NAME, 'name')
item_description_input = (By.XPATH, './/textarea[@class="textarea_inputStandart__IoNxq spanGlobal"]')
item_price_input = (By.NAME, 'price')

# Профиль
profile_name = (By.XPATH, ".//h3[@class='profileText name']")
profile_avatar = (By.XPATH, ".//button[@class='circleSmall']//*[name()='svg']")
profile_avatar_button = (By.XPATH, ".//button[@class='circleSmall']")

# Ошибки
error_input = (By.XPATH, './/div[@class="input_inputError__fLUP9"]')
error_input_text = (By.CLASS_NAME, "input_span__yWPqB")

# Дропдауны
dropdown_menu = (By.XPATH, './/button[@class="dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP"]')
dropdown_category_selected = (By.XPATH, './/span[@class="undefined dropDownMenu_textColor__Nyo8k" and text()="Садоводство"]')
dropdown_city_selected = (By.XPATH, './/span[@class="undefined dropDownMenu_textColor__Nyo8k" and text()="Санкт-Петербург"]')

# Мои объявления
created_item_text = (By.XPATH, './/div[@class="about"]/h2')

# Ожидания
element_card_is_located = (By.CLASS_NAME, 'card')

# Попап авторизации для размещения объявления
popup_auth_before_create_item = (By.CLASS_NAME, 'popUp_titleRow__M7tGg')
popup_auth_before_create_item_text = (By.XPATH, ".//div[@class='popUp_titleRow__M7tGg']//h1[@class='h1']")