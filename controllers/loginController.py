from flask import Blueprint
from flask import render_template
from flask import request, session, redirect, url_for
from routes import menu


loginController = Blueprint("loginController", __name__)


@loginController.route('/login', methods=['POST', 'GET'])
def login():
    """
    Обрабатывает функциональность входа в систему.

    Параметры:
    - Нет

    Возвращает:
    - Если пользователь уже авторизован, перенаправляет на страницу профиля
        пользователя.
    - Если метод запроса POST, устанавливает переменную сеанса 'userLogged'
        и перенаправляет на страницу профиля пользователя.
    - В противном случае, отображает страницу входа с указанным
        заголовком и меню.

    """
    if 'userLogged' in session:
        return redirect(url_for(
            'profileController.profile',
            username=session['userLogged']
        ))
    elif request.method == 'POST':
        session['userLogged'] = request.form['username']
        return redirect(
            url_for(
                'profileController.profile',
                username=session['userLogged']
            )
        )

    return render_template('login.html', title='Авторизация', menu=menu)
