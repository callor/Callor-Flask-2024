from flask import Blueprint, render_template
from databases.models import Question

# 블루프린터 생성
# router 를 분리하기 위해 블루프린터를 생성하여 사용한다
bp = Blueprint('main', __name__, url_prefix='/')

# 블루프린터 router
@bp.route("/") # route() 데코레이터로 어떤 URL이 함수를 트리거해야 하는지 Flask에 알림
def home():
    return """<h3>안녕하세요 반갑습니다!</h3>
            <p>여기는 FLask Home 입니다</p>
    """ #사용자의 브라우저에 표시하려는 메시지 반환


