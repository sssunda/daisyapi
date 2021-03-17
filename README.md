# DaisyAPI

DaisyAPI is a web application server for studying about testing and prototyping.


It is implemented based on the flask web framework.


## Project Setting
1. 가상 환경 준비 및 필요 패키지 설치 (virtualenv)
1. setup.py 생성
1. lint 설정 추가 (pylint, flake8)
1. Pre-commit 설정 파일 추가
1. Makefile 추가
1. Dockerfile 추가
1. 테스트 추가 (pytest)
1. 테스트 자동화 (travis-ci)

### 가상 환경 준비 및 필요 패키지 설치 (virtualenv)
```bash
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install Flask
$ pip freeze > requirements.txt
```

### setup.py 생성
```bash
$ pip install -e .
```

### lint 설정 추가 (pylint, flake8)
```bash
$ pip install pylint # pylintrc 추가
$ pip install flake8 # setup.cfg 추가
```

### Pre-commit 설정 파일 추가
```bash
$ pip install pre-commit
$ pre-commit install # .pre-commit-config.yaml 추가
```

### Makefile 추가
```bash
$ touch Makefile 
```

### Dockerfile 추가
```bash
$ touch Dockerfile
```

### 테스트 추가 (pytest)
```bash
$ pip install pytest # conftest.py 로 세팅
```
