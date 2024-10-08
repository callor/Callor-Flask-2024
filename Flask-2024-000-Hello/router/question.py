from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from datetime import datetime


from app import db
from databases.models import Question
from modules.forms import QuestionForm

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/create', methods=('GET',))
def question():

    # form 의 input field 에 데이터 표시하기위해 초기 데이터 생성
    question = Question(subject="글쓰기",content="안녕하세요")
    # form 에 data 삽입하기
    form = QuestionForm(obj=question)
    # form 화면에 그리기
    return render_template('question/question_input.html', form=form)

@bp.route('/create', methods=('POST',))
def question_post():
    form = QuestionForm()
    subject = form.subject.data
    content = form.content.data
    create_date=datetime.now()
    print("subject=",subject,"content=",content,create_date)

    question_data = Question(subject=subject, content=content,create_date=create_date)
    result = db.session.add(question_data)
    db.session.commit()
    print(result)

    return redirect("/question")


