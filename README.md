# Python 기초 공부 프로젝트

Python 기초를 익혀서 API 호출 → 데이터 처리 → 응답 반환까지 가능하도록 하는 프로젝트입니다.

**🕐 학습 기간**: 약 2주

---

## 🎯 최종 목표

> API 호출 → 데이터 처리 → 응답 반환 가능

---

## 📅 학습 일정

### Day 1~3: Python 핵심 문법

#### 학습 내용
- 변수 / 리스트 / 딕셔너리
- 함수
- 클래스 (기초)
- 파일 입출력

#### 포인트
- JavaScript와 비교하며 학습
- 깊이보다 "익숙해지는 것"이 중요

---

### Day 4~5: API 활용

#### 학습 내용
- requests 라이브러리
- JSON 파싱

#### 예시 코드
```python
import requests

res = requests.get("https://api.example.com")
data = res.json()
print(data)
```

#### 학습 목표
✅ 외부 API 데이터를 가져와 가공할 수 있다

---

### Day 6~7: FastAPI

#### 학습 내용
- 서버 생성
- 라우팅

#### 예시 코드
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello"}
```

#### 학습 목표
✅ 간단한 API 서버 구축

---

## 📚 참고 자료

- [Python 공식 문서](https://docs.python.org/3/)
- [requests 라이브러리](https://requests.readthedocs.io/)
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
