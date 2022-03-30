# yt_simple_web_service

### > 준비

- 해당 repository를 clone 후 사용하시는 가상환경을 실행합니다.
- `pip install -r requirements.txt` 명령어를 터미널에 입력하여 본 프로젝트에서 사용된 버전의 패키지들을 받습니다.

<br/>

### > 환경설정

- 개발보드 기준 root경로에 .env 파일을 만든 후 아래 양식을 채워주면 됩니다.

```
FLASK_APP = app.py
FLASK_ENV = development

# 문자열을 문자열("") 기호로 감싸지 않아도 됩니다.
DB_USER     = 유저 id
DB_PASSWORD = 비밀번호
DB_HOST     = 호스트명
DB_NAME     = db 이름
DB_PORT     = 포트번호

WEB_HOST = localhost
WEB_PORT = 5000

DEBUG = True
```

<br/>

### > 실행

```
$ flask run
```
