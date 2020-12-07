from flask import Flask

from ddd_attempt1.rest import storageroom
from ddd_attempt1.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(storageroom.blueprint)
    return app
