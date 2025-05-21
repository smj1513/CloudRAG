import pytest
from agent import Agent

def test_agent_initialization():
    """에이전트가 정상적으로 초기화되는지 테스트"""
    agent = Agent()
    assert agent is not None

def test_agent_methods():
    """에이전트의 기본 메서드들이 존재하는지 테스트"""
    agent = Agent()
    assert hasattr(agent, 'process')
    assert hasattr(agent, 'respond') 