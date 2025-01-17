# Сравниваем вакансии программистов

Скрип предназначен для подсчета статистики по средней заработной плате программистов в зависимости от языка
программирования. Поиск вакансий осуществляется на площадках [HeadHunter](https://hh.ru/)
и [Superjob](https://www.superjob.ru/) в городе Москве.

### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

Далее добавьте в папку с проектом файл `.env` и скопируйте туда следующий код:

```
SUPERJOB_API_KEY=""
```

SUPERJOB_API_KEY - можно получить, зарегистрировавшись на сайте [Superjob](https://api.superjob.ru). Далее необходимо
зарегистрировать приложение. После регистрации необходима строчка - `Secret key`

### Пример работы скрипта

Для запуска вводим в консоль команду:
```
python main.py
```
После запуска скрипта результат выведется не моментально.

По окончанию работы в консоле выведутся две таблицы. Пример ниже:

![image](https://github.com/user-attachments/assets/a0bfb7ba-eacb-4117-8c24-514df853d5b0)

![image](https://github.com/user-attachments/assets/65830986-7e93-48cf-9f7b-b3b05edc2bea)

### Цель проекта

Код написан в образовательных целях.
