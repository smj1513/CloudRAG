# CloudRAG 프로젝트

이 프로젝트는 클라우드 기반의 RAG(Retrieval-Augmented Generation) 시스템을 구현한 것입니다.

## 사전 요구사항

- Python 3.8 이상
- pip (Python 패키지 관리자)
- Docker (선택사항)

## 설치 방법

1. 프로젝트 클론
```bash
git clone [프로젝트_저장소_URL]
cd cloudRAG
```

2. 가상환경 생성 및 활성화
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

## 실행 방법

### 로컬 환경에서 실행

1. 가상환경이 활성화된 상태에서 다음 명령어를 실행합니다:
```bash
python main.py
```

### Docker를 사용한 실행

1. Docker 이미지 빌드
```bash
docker build -t cloudrag-app .
```

2. Docker 컨테이너 실행
```bash
docker run -p 8000:8000 cloudrag-app
```

## 프로젝트 구조

- `main.py`: 메인 애플리케이션 파일
- `agent.py`: RAG 에이전트 구현
- `llm.py`: LLM 관련 기능
- `tools.py`: 유틸리티 도구
- `config.py`: 설정 파일
- `requirements.txt`: 프로젝트 의존성 목록
- `Dockerfile`: Docker 이미지 빌드 설정

## 주의사항

- 실행하기 전에 필요한 API 키와 환경 변수가 올바르게 설정되어 있는지 확인하세요.
- 대용량 파일 처리 시 충분한 메모리가 필요할 수 있습니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 