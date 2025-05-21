from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from config import prompt
from tools import tools
from typing import Generator
import time

def create_agent():
    """
    에이전트를 생성하고 설정합니다.
    """
    # LLM 모델 초기화
    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        streaming=True,
        temperature=0.7
    )
    
    # 에이전트 생성
    agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
    
    # AgentExecutor 생성
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=10,
        max_execution_time=10,
        handle_parsing_errors=True,
    )
    
    return agent_executor

def stream_text(text: str, chunk_size: int = 5) -> Generator[str, None, None]:
    """
    텍스트를 작은 청크로 나누어 스트리밍합니다.
    
    Args:
        text (str): 스트리밍할 텍스트
        chunk_size (int): 각 청크의 크기
        
    Yields:
        str: 텍스트 청크
    """
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]
        time.sleep(0.05)  # 각 청크 사이에 약간의 지연 추가

def run_agent(agent_executor, query: str) -> Generator[str, None, None]:
    """
    에이전트를 실행하고 결과를 스트리밍 형식으로 반환합니다.
    
    Args:
        agent_executor: AgentExecutor 인스턴스
        query (str): 사용자 질문
        
    Yields:
        str: 스트리밍되는 응답 텍스트
    """
    try:
        full_response = ""
        for chunk in agent_executor.stream({"input": query}):
            if "output" in chunk:
                new_text = chunk["output"][len(full_response):]
                full_response = chunk["output"]
                for text_chunk in stream_text(new_text):
                    yield text_chunk
    except Exception as e:
        error_message = f"죄송합니다. 오류가 발생했습니다: {str(e)}"
        for chunk in stream_text(error_message):
            yield chunk 