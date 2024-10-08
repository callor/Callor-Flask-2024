from flask import Flask #flask 클래스 가져옴
from flask import render_template # jinja2 


# Flask 애플리케이션 팩토리
# 이 함수이름은 고정이다(변경금지)
def create_app():

    app = Flask(__name__) #flask 클래스의 인스턴스 생성. 이 인스턴스는 WSGI 애플리케이션이 됨


    # router 분리하기
    from router import home,books

    # 블루프린터(router) 등록    
    app.register_blueprint(books.bp)
    app.register_blueprint(home.bp)
        
    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name) #템플릿 뿌려주기 위해 render_template() 메소드 사용

    return app

