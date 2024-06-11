from pyms.flask.app import Microservice

ms = Microservice()
app = ms.create_app()

from controllers.login_controller import login_blueprint
from controllers.user_controller import user_blueprint

app.register_blueprint(login_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    app.run(port=5001)
