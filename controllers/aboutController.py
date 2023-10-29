from flask import Blueprint
from flask import render_template
from routes import menu


aboutController = Blueprint("aboutController", __name__)


@aboutController.route('/about')
def about():
    """
    Отображает шаблон 'about.html' с указанным заголовком и меню.

    Возвращает:
        Отображаемая HTML-страница.
    """
    return render_template('about.html', title='О нас', menu=menu)
