# Flask Web Application Project

@since 2024.10

## 플라스크 ORM 라이브러리 사용하기

파이썬 ORM 라이브러리 중 가장 많이 사용하는 SQLAlchemy를 사용해 보자. 이와 더불어 파이썬 모델을 이용해 테이블을 생성하고 컬럼을 추가하는 등의 작업을 할 수 있게 해주는 Flask-Migrate 라이브러리도 사용해 보자.

### ORM 라이브러리 설치하기

Flask-Migrate 라이브러리를 설치하면 SQLAlchemy도 함께 설치되므로 myproject 가상 환경에서 다음 명령을 수행하여 Flask-Migrate 라이브러리를 설치하자.

```sh
c:\projects\myproject>pip install flask-migrate
Collecting Flask-Migrate
(... 생략 ...)
```

## 설정 파일 추가하기

파이보에 ORM을 적용하려면 데이터베이스 설정이 필요하다. 루트 디렉터리에 config.py 파일을 생성하고 다음과 같은 코드를 작성하자.

[파일명: projects/myproject/config.py]

```py
import os

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'mydb.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소이고
# SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트를 처리하는 옵션이다.
# 이 옵션은 파이보에 필요하지 않으므로 False로 비활성화하자.
# SQLALCHEMY_DATABASE_URI 설정에 의해 SQLite 데이터베이스가 사용되고 데이터베이스 파일은
# 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장된다.
```

### SQLite는 어떤 데이터베이스일까?

파이썬 기본 패키지에 포함된 SQLite는 주로 소규모 프로젝트에서 사용하는 가벼운 파일을 기반으로 한 데이터베이스다. 보통은 SQLite로 개발을 빠르게 진행하고 이후 실제 운영 시스템에 반영할 때에는 좀 더 규모가 큰 데이터베이스로 교체한다.

## 데이터베이스 초기화하기

이제 ORM을 사용할 준비가 되었으므로 flask db init 명령으로 데이터베이스를 초기화하자.

```sh
(myproject) c:\projects\myproject>flask db init
Creating directory c:\projects\myproject\migrations ...  done
Creating directory c:\projects\myproject\migrations\versions ...  done
Generating c:\projects\myproject\migrations\alembic.ini ...  done
Generating c:\projects\myproject\migrations\env.py ...  done
Generating c:\projects\myproject\migrations\README ...  done
Generating c:\projects\myproject\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'c:\\projects\\myproject\\migrations\\alembic.ini' before proceeding.
```

flask db init 명령은 데이터베이스를 관리하는 초기 파일들을 다음처럼 migrations 디렉터리에 자동으로 생성한다.

## 데이터베이스 관리 명령어 정리하기

앞으로 모델을 추가하거나 변경할 때는 flask db migrate 명령과 flask db upgrade 명령만 사용할 것이다. 즉, 앞으로 데이터베이스 관리를 위해 여러분이 반드시 알아야 할 명령어는 다음 2가지이다.

| 명령어           | 설명                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| flask db migrate | 모델을 새로 생성하거나 변경할 때 사용 (실행하면 작업파일이 생성된다.)                                              |
| flask db upgrade | 모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용 (위에서 생성된 작업파일을 실행하여 데이터베이스를 변경한다.) |

이 밖에도 여러 명령이 있지만 특별한 경우가 아니라면 이 2가지 명령어를 주로 사용할 것이다. 명령어 종류를 확인하고 싶다면 명령 프롬프트에서 flask db 명령을 입력해 보자.

## 모델 import

모델 파일은 app 폴더에 작성한다
앞에서 작성한 모델을 플라스크의 migrate 기능이 인식하려면 다음과 같은 import 과정이 필요하다.

[파일명: projects/myproject/pybo/__init__.py]

```py
(... 생략 ...)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

(... 생략 ...)
```

## 리비전 파일 생성하기

그리고 명령 프롬프트에서 flask db migrate 명령을 수행하자.

```sh
(myproject) c:\projects\myproject> flask db migrate
INFO [alembic.runtime.migration] Context impl SQLiteImpl.
INFO [alembic.runtime.migration] Will assume non-transactional DDL.
INFO [alembic.autogenerate.compare] Detected added table ‘question’
INFO [alembic.autogenerate.compare] Detected added table ‘answer’
Generating c:\projects\myproject\migrations\versions\18634a293520_.py ... done
```

## 리비전 파일 실행하기

이어서 flask db upgrade 명령으로 만들어진 리비전 파일을 실행하자. (리비전 파일 내에는 테이블 생성을 위한 쿼리문들이 저장되어 있다.)

```sh
(myproject) c:\projects\myproject> flask db upgrade
INFO [alembic.runtime.migration] Context impl SQLiteImpl.
INFO [alembic.runtime.migration] Will assume non-transactional DDL.
INFO [alembic.runtime.migration] Running upgrade -> 18634a293520, empty message
```

이 과정에서 데이터베이스에 모델 이름과 똑같은 question과 answer라는 이름의 테이블이 생성된다. 지금까지 잘 따라왔다면 projects/myproject 디렉터리에 pybo.db 파일이 생성되었을 것이다. pybo.db가 바로 SQLite 데이터베이스의 데이터 파일이다.

## Flask input form 만들기

```sh
pip install -U Flask-WTF
```
