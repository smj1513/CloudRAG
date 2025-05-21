import os
import sys
from pathlib import Path

# 프로젝트 루트 디렉토리를 Python 경로에 추가
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

# 테스트용 환경 변수 설정
os.environ['OPENAI_API_KEY'] = 'test-openai-key'
os.environ['TAVILY_API_KEY'] = 'test-tavily-key' 