from flask import Blueprint
from flask import render_template
from routes import menu

indexController = Blueprint("indexController", __name__)


@indexController.route('/index')
@indexController.route('/')
def index():
    """
    Функция, которая является обработчиком маршрута '/index' и '/'.
    Она отображает шаблон 'index.html' с указанным заголовком и меню.
    Эта функция не принимает параметров и возвращает отрендеренный шаблон.

    Возвращает:
        render_template object: Отрендеренный шаблон 'index.html'.
    """

    return render_template('index.html', title='Главная', menu=menu)
