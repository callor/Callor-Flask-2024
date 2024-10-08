from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app import db
from databases.models import Question
from modules.forms import QuestionForm

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/create', methods=('GET',))
def question():
    question = Question()
    # question.subject = '메롱'
    form = QuestionForm(obj=question)
    return render_template('question/question_input.html', form=form)

@bp.route('/create', methods=('POST',))
def question_post():
    form = QuestionForm()
    subject = form.subject.data
    content = form.content.data
    print("subject=",subject,"content=",content)

    question_data = Question(subject=subject, content=content)
    db.session.add(question_data)

    return redirect("/")


