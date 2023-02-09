# IntensiveYandex-django

![example event parameter](https://github.com/maryshirk/IntensiveYandex-django/actions/workflows/python-package.yml/badge.svg)

## Инструкция по запуску проекта в dev-режиме

### 1. Клонирование
```
git clone https://github.com/maryshirk/IntensiveYandex-django
```

### 2. Активация виртуальной среды
```
python -m venv venv
```
Mac OS/Linux:
```
source venv/bin/activate
```
Windows:
```
.\venv\Scripts\activate
```

### 3. Установка requirements
Чтобы запустить проект
```
pip install -r requirements.txt
```
Для разработки
```
pip install -r requirements_developer.txt
```
Чтобы проверить тесты
```
pip install -r requirements_test.txt
```

### 4. Генерация файла с переменными виртуальной среды (.env)
Создайте файл ".env" в корневом каталоге со структурой, указанной в файле ".env_example", указав секретный ключ, наличие дебаг-режима и электронную почту.

### 5. Запуск
```
python lyceum/manage.py runserver
```
