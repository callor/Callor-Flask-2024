from flask import Blueprint


# 블루프린터 생성
# router 를 분리하기 위해 블루프린터를 생성하여 사용한다
bp = Blueprint('books', __name__, url_prefix='/books')

# 블루프린터 router
@bp.route("/") # route() 데코레이터로 어떤 URL이 함수를 트리거해야 하는지 Flask에 알림
def home():
    return "<p>여기는 book Home 입니다</p>" #사용자의 브라우저에 표시하려는 메시지 반환
