from flask import Blueprint
from flask import render_template
from flask import flash, request
from routes import menu


contactController = Blueprint("contactController", __name__)


@contactController.route('/contact', methods=['POST', 'GET'])
def contact():
    """
    Создает маршрут для обработки запросов на '/contact' с методами 'POST' и 'GET'.

    Параметры:
        Нет

    Возвращает:
        Отображаемый шаблон 'contact.html' с заголовком 'Контакты' и меню, заданное значением 'menu'.

    Исключения:
        Нет
    """
    error = []
    if (request.method == 'POST'):
        if (request.form['name'] == ''):
            error.append('Имя не может быть пустым')

        if (request.form['email'] == ''):
            error.append('Email не может быть пустым')

        if (request.form['message'] == ''):
            error.append('Сообщение не может быть пустым')

        if (len(error) == 0):
            flash('Сообщение отправлено!', category='alert-success')
        else:
            for e in error:
                flash(e, category='alert-error')

    return render_template(
        'contact.html',
        title='Контакты',
        menu=menu
    )
