from flask import Blueprint
from flask import render_template
from flask import session, abort
from routes import menu


profileController = Blueprint("profileController", __name__)


@profileController.route('/profile/<username>')
def profile(username):
    """
    Рендерит страницу профиля для указанного имени пользователя.

    Параметры:
    - username (str): Имя пользователя для отображения профиля.

    Возвращает:
    - Если пользователь авторизован и имя пользователя в сессии
        совпадает с указанным именем пользователя, то возвращается
        отрендеренная страница профиля.
    - Если пользователь не авторизован или имя пользователя в
        сессии не совпадает с указанным именем пользователя, то
        запрос прерывается с ошибкой 403.
    """
    if 'userLogged' in session and session['userLogged'] == username:
        return render_template(
            'profile.html',
            title='Профиль',
            username=username,
            menu=menu
        )
    else:
        abort(403)
