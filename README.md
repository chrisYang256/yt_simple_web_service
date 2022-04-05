# yt_simple_web_service

</br>

## > 준비

- 터미널에서 프로젝트를 저장할 위치로 이동하여 해당 repository를 clone합니다.

- `pip install -r requirements.txt` 명령어를 터미널에 입력하여 본 프로젝트에서 사용된 버전의 패키지들을 받습니다.

</br>
</br>

## > 환경설정

- 프로젝트 root 경로에 .env 파일을 만든 후 아래 양식을 채워줍니다.

```terminal
# config for dev
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

</br>
</br>

## > 실행

- venv 등 사용하시는 가상환경을 실행합니다.

- 터미널 위치를 프로젝트 root 경로로 이동 후 아래 명령어를 실행합니다.

```terminal
flask run
```

- 브라우저 주소란에 아래와 같이 입력한 후 이동하면 프로젝트를 실행할 수 있습니다.

  - 회사 관련: "localhost:포트번호/company/list_view

  - 유저 관련: "localhost:포트번호/user/list_view
