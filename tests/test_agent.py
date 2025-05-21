import pytest
from agent import Agent

@pytest.fixture
def agent_instance():
    """테스트용 Agent 인스턴스 생성"""
    return Agent()

def test_agent_initialization(agent_instance):
    """에이전트가 정상적으로 초기화되는지 테스트"""
    assert agent_instance is not None

def test_agent_methods(agent_instance):
    """에이전트의 기본 메서드들이 존재하는지 테스트"""
    assert hasattr(agent_instance, 'process')
    assert hasattr(agent_instance, 'respond') 