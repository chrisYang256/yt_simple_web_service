# yt_simple_web_service

### > 설치

- 해당 repository를 클론한 후 사용하시는 가상환경을 실행합니다.
- `pip install -r requirements.txt` 명령어를 터미널에 입력하여 본 프로젝트에서 사용된 버전의 패키지들을 받습니다.

<br/>

### > 환경설정

- 개발보드 기준 root경로에 .env.dev 파일을 만든 후 아래 양식을 채줘주면 됩니다.

```
FLASK_APP = app.py
FLASK_ENV = development

DB_USER      = "유저 id"
DB_PASSWORD  = "비밀번호"
DB_HOST      = "호스트명"
DB_NAME      = "db 이름"
DB_PORT      = 포트번호
```
