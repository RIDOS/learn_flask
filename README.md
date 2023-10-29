# Простое WSGI-приложение на Flask

## О проекте
Проект выполнялся для изучения фреимворка `flask`.

## Запуск проекта

Создайте виртальное окружение `venv` командой:
```bash
python3 -m venv venv && source venv/bin/activate
```

Установите нужные библиотеки командой:
```bash
pip install -r requirements.txt
```

Добавьте файл `.env` и вставьте свой секретный ключ:
```bash
cp .env.test .env
```

Запустите приложеине командой:
```bash
python3 app.py
```

## Структура проекта

- Исполняемый файл `app.py` импортирует все контроллеры и
    запускает `flask` приложение.
- Все маршруты прописаны в файле `routes.py`.
- В папке `controllers` находятся исполняемые файлы для обработки
    запросов пользователя.
- В папке `templates` находятся шаблоны `html` документов.
- В папке `static` находятся скрипты и стили приложения.

```
├── app.py
├── controllers
│   ├── aboutController.py
│   ├── contactController.py
│   ├── indexController.py
│   ├── loginController.py
│   ├── profileController.py
├── db
├── routes.py
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── script.js
└── templates
    ├── 404.html
    ├── about.html
    ├── base.html
    ├── contact.html
    ├── index.html
    ├── login.html
    └── profile.html
```
