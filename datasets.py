# Список ящиков, не подходящих под условие с форматом почты, список для примера, можно расширять, 
# некоторые ситуации убрал, так как у них получалось пройти регистрацию
wrong_emails = ['@gmail.com', 'test@.com', 'test_email_gmail.com', 
                'test@...com', 'test@mail.', 'test@mail.c', 'test@mail.123'
                'test@-mail.com', 'test@@mail.com', 'test@mail .com']

# Существующий пользователь и его данные
exist_user = {'email':'exist_user@gmail.com', 'password':111222}