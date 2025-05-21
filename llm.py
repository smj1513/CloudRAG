from agent import create_agent, run_agent
from typing import Generator

# 에이전트 인스턴스 생성
agent_executor = create_agent()

def get_ai_response(user_question: str) -> Generator[str, None, None]:
    """
    사용자의 질문에 대한 AI 응답을 스트리밍 형식으로 생성합니다.
    
    Args:
        user_question (str): 사용자의 질문
        
    Yields:
        str: 스트리밍되는 AI의 응답
    """
    try:
        for chunk in run_agent(agent_executor, user_question):
            yield chunk
    except Exception as e:
        yield f"죄송합니다. 오류가 발생했습니다: {str(e)}" 