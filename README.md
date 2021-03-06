# FinalPractice-Project-DNS-shop
50 тестов, которые проверяют некоторый функционал сайта DNS

Общая структура проекта:

1. Папка Config содержит основные переменные тестирования:

!!!ВАЖНО!!!
Часть тестов требует авторизацию. В нижеуказанном файле config.py в соответсвующих переменных необходимо вписать валидные почту и пароль (по умолчанию там неверные данные)
Также необходимо указать свой путь до Chromedriver в соответствующей переменной (CHROME_EXECUTABLE_PATH)

1.1 config.py - три главные тестируемые страницы (главная, профиль, корзина) + различные переменные, которые вводятся пользователем (логин, пароль, параметры поиска, параметры проверки некоторых тестов, параметры фильтров)
1.2 locators.py - файл со всеми локаторами тестов.

2. Папка Pages содержит все методы для тестов:
2.1 BasePage.py - все основные методы тестирования, которые служат конструктором для более сложных методов
2.1.1 HomePage.py - методы тестирования для главной страницы (авторизация, поиск, фильтрация товара)
2.1.2 ProfilePage.py - методы тестирования для страницы профиля пользователя
2.1.3 SearchPage.py - метод тестирования для поиска товара
2.1.4 CartPage.py - методы тестирования для корзины товара

3. Папка Tests содержит все тесты:
3.1 conftest.py - двигатель проекта, содержащий главную фикстуру проекта
3.1.1 test_base.py - содержит главный класс BaseTest для тестирования
3.2 test_HomePage.py - 10 тестов на авторизацию пользователя, 12 тестов на поиск товара (с параметризацией), 20 тестов с использованием каталога товаров и фильтрацией
3.3 test_ProfilePage.py - 3 теста профиля пользователя, один с багом (использование фикстуры mark.xfail)
3.4 test_CartPage.py - 4 теста корзины товаров
3.5 test_ComplexTests.py - 2 итоговых теста: дымовое тестирование (самый короткий сценарий оформления заказа) и комплексный тест с авторизацией, проверкой профиля пользователя, добавлением товара в корзину, удалением товара из корзины, разлогином пользователя

Каждый тест в проекте после assert'a имеет своё описание, в котором указывается суть теста, а также на что происходит проверка.

__________________________________________________________
Немного пояснения: понимание и осознание как сделать лучше тесты, приходило по мере выполнения итоговой работы. Если сначало тесты попроще, то в конце они, как мне кажется, посложнее (как минимум с несколькими проверками). Проследить хронолгию проекта можно по номерам тестов указанным в "print'ах".
Сейчас вижу "узкие места в логике некоторых тестов". Например, с открытым или закрытым профилем (если стартовые условия задуманные тестировщиком не соответствуют необходимым, то тест провалится: так если изначально профиль закрыт, то тест на закрытие профиля провалится изза неверного ассерта. Вероятно можно было бы испаривть тест, через оператор "if", но к сожалению уже не успеваю - надо сдавать работу. Тесты с добавлением в корзину лучше делать без авторизации, поскольку тогда товар сохраняется в корзине пользователя и в последствии может повлиять на assert'ы и так далее.
