from flask import Flask #flask 클래스 가져옴
from flask import render_template # jinja2 


# SQLite DB 적용하기
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, CSRFError

import os

import config

db = SQLAlchemy()
migrate = Migrate()

# Flask 애플리케이션 팩토리
# 이 함수이름은 고정이다(변경금지)
def create_app():

    app = Flask(__name__) #flask 클래스의 인스턴스 생성. 이 인스턴스는 WSGI 애플리케이션이 됨

    # form 에 csrf Token 부여하기
    csrf = CSRFProtect(app)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    # DB config 로딩
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # model import
    from databases import models

    # router 분리하기
    from router import home,books,question

    # 블루프린터(router) 등록    
    app.register_blueprint(books.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(question.bp)
        
    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name) #템플릿 뿌려주기 위해 render_template() 메소드 사용

    return app

