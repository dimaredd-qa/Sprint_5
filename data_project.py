import random
import string
#здесь будут данные логин пароль для тестов и юрлки
class Credential:
    name = 'Slipenberg'
    email = 'slipenberg25062025@yandex.ru'
    password = '11112222'


class Site:
    main_site = 'https://stellarburgers.nomoreparties.site/'
    registration_site = f'{main_site}register'
    profile_site = f'{main_site}account/profile'
    login_site = f'{main_site}login'
    password_recovery_site= f'{main_site}forgot-password'
    #Лента заказов
    table_order = f'{main_site}feed'


class RandomEmailPassword:

    def __init__(self):
        self.name = None
        self.email = None
        self.cohort = 25
        self.password = None

    def generate(self):
        if self.name is None and self.email is None and self.password is None:

            name_length = random.randint(8, 12)
            self.name = ''.join(random.choices(string.ascii_lowercase, k=name_length))

            letters_length = random.randint(10, 15)
            letters_part = ''.join(random.choices(string.ascii_lowercase, k=letters_length))
            digits_part = ''.join(random.choices(string.digits, k=3))
            self.email = f'{letters_part}{self.cohort}_{digits_part}@example.com'

            password_length = random.randint(8, 12)
            self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

        return self.name, self.email, self.password

#Проверка генерации
#generator = RandomEmailPassword()
#email, password = generator.generate()
#print("Email:", email)
#print("Password:", password)