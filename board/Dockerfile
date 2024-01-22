# 기본 이미지로 Python 이미지를 사용
FROM python:3.9

# 작업 디렉토리를 /app으로 설정
WORKDIR /app

# 필요한 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 소스코드를 현재 작업 디렉토리로 복사
COPY . .
COPY static static
# FastAPI 서버 실행
CMD ["uvicorn", "board_app:app", "--host", "0.0.0.0", "--port", "8000"]
