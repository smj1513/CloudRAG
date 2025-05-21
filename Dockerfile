FROM python:3.11-slim

WORKDIR /app

# 필수 시스템 패키지 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# pip 업그레이드 및 필요한 파일 복사
RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 파일 복사
COPY *.py .
COPY embedding_vectors/ ./embedding_vectors/

# 포트 설정
EXPOSE 80

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# 애플리케이션 실행
CMD ["streamlit", "run", "main.py", "--server.port=80", "--server.address=0.0.0.0"] 