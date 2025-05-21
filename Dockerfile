FROM python:3.9-slim

WORKDIR /app

# 환경 변수 설정
ARG OPENAI_API_KEY
ARG TAVILY_API_KEY
ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV TAVILY_API_KEY=$TAVILY_API_KEY

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 포트 설정
EXPOSE 8000

# 애플리케이션 실행
CMD ["streamlit", "run", "main.py", "--server.port=8000", "--server.address=0.0.0.0"] 