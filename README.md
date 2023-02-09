# IntensiveYandex-django

![example workflow](https://github.com/maryshirk/IntensiveYandex-django/blob/main/.github/workflows/python-package.yml/badge.svg)

## Инструкция по запуску проекта в dev-режиме

### 1. Клонирование
git clone https://github.com/maryshirk/Yandex_Intensive_Django/tree/HW1

### 2. Активация виртуальной среды
python -m venv venv
Mac OS/Linux:
source venv/bin/activate
Windows:
.\venv\Scripts\activate

### 3. Установка requirements
pip install -r requirements.txt

### 4. Генерация файла с переменными виртуальной среды (.env)
Сгенерируйте файл '.env' в корневом каталоге со структурой, указанной в 'Yandex_Intensive_Django\hw1\hw1\hw1\.env'

### 5. Запуск
python hw1/manage.py runserver
