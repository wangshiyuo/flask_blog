from flask import Flask
from app.models.all_models import db


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def creat_app():
    app = Flask(__name__)

    # 导入配置文件
    app.config.from_object('secure')
    app.config.from_object('settings')

    #注册蓝图
    register_blueprint(app)

    # 注册SQLAlchemy
    db.init_app(app)
    db.create_all(app=app)

    return app
