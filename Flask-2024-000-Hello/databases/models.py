from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


# question_id 속성은 답변을 질문과 연결하기 위해 추가한 속성이다. 
# 답변은 어떤 질문에 대한 답변인지 알아야 하므로 질문의 id 속성이 필요하다. 
# 그리고 모델을 서로 연결할 때에는 위와 같이 db.ForeignKey를 사용해야 한다.

# question 속성은 답변 모델에서 질문 모델을 참조하기 위해 추가했다. 
# 위와 같이 db.relationship으로 question 속성을 생성하면 답변 모델에서 연결된 질문 모델의 제목을 
# answer.question.subject처럼 참조할 수 있다.
# db.relationship의 첫 번째 파라미터는 참조할 모델명이고 
# 두 번째 backref 파라미터는 역참조 설정이다. 
# 역참조란 쉽게 말해 질문에서 답변을 거꾸로 참조하는 것을 의미한다. 
# 한 질문에는 여러 개의 답변이 달릴 수 있는데 역참조는 이 질문에 달린 답변들을 참조할 수 있게 한다. 
# 예를 들어 어떤 질문에 해당하는 객체가 a_question이라면 a_question.answer_set와 같은 코드로 
# 해당 질문에 달린 답변들을 참조할 수 있다.

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


# flask db migrate    