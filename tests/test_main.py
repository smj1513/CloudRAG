import pytest
from main import app

def test_app_initialization():
    """애플리케이션이 정상적으로 초기화되는지 테스트"""
    assert app is not None

def test_environment_variables():
    """필수 환경 변수가 설정되어 있는지 테스트"""
    import os
    assert 'OPENAI_API_KEY' in os.environ
    assert 'TAVILY_API_KEY' in os.environ 