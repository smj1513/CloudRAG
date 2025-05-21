import pytest
import os
from main import app

@pytest.fixture
def app_instance():
    """테스트용 app 인스턴스 생성"""
    return app

def test_app_initialization(app_instance):
    """애플리케이션이 정상적으로 초기화되는지 테스트"""
    assert app_instance is not None

def test_environment_variables():
    """필수 환경 변수가 설정되어 있는지 테스트"""
    assert 'OPENAI_API_KEY' in os.environ
    assert 'TAVILY_API_KEY' in os.environ 