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

### Цель проекта

Код написан в образовательных целях.