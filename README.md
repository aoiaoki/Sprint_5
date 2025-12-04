# Автотесты для Stellar Burgers

Проект содержит автотесты на Selenium + Pytest для веб-приложения [Stellar Burgers](https://stellarburgers.education-services.ru/). Тестируются основные сценарии: регистрация, вход в аккаунт, проверка профиля, навигация и валидация полей формы.

---

## Структура проекта

Sprint_5/
├── locators/ # Локаторы для страниц
│ ├── main_page.py
│ ├── login_page.py
│ ├── register_page.py
│ ├── profile_page.py
│ └── forgot_password.py
├── tests/ # Тесты
│ ├── test_login.py
│ ├── test_registration.py
│ ├── test_profile.py
| └── test_constructor.py
├── generator.py # Генератор email и паролей для регистрации
└── README.md
