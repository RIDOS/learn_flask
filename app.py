from flask import Flask
from flask import render_template
from controllers.indexController import indexController
from controllers.aboutController import aboutController
from controllers.contactController import contactController
from controllers.loginController import loginController
from controllers.profileController import profileController

from dotenv import dotenv_values

config = dotenv_values('.env')

app = Flask(__name__)
app.secret_key = config['SECRET_KEY']


app.register_blueprint(indexController)
app.register_blueprint(aboutController)
app.register_blueprint(contactController)
app.register_blueprint(loginController)
app.register_blueprint(profileController)


@app.errorhandler(404)
def pageNotFoud(error):
    """
    Функция для обработки ошибки, когда страница не найдена.

    Параметры:
        error (объект): Объект ошибки.

    Возвращает:
        объект: Шаблон 404.html, отрендеренный с указанным заголовком и меню.
    """
    return render_template('404.html', title='Страница не найдена')


if __name__ == "__main__":
    app.run(debug=True)
