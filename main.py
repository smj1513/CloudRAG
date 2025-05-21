import streamlit as st

from llm import get_ai_response
from agent import create_agent, run_agent

def init_session_state():
    """
    세션 상태를 초기화합니다.
    """
    if 'message_list' not in st.session_state:
        st.session_state.message_list = []

def render_sidebar():
    """
    사이드바를 렌더링합니다.
    """
    with st.sidebar:
        st.header("ℹ️ 사용 방법")
        st.markdown("""
        1. 채팅창에 질문을 입력하세요
        2. AI가 공공기관 채용 정보를 검색하여 답변해드립니다
        3. 예시 질문:
            - 2025년 공공기관 전산직 채용 정보 알려줘
            - 한국철도공사 채용 일정이 어떻게 되나요?
            - 공공기관 신입 채용 연봉은 얼마인가요?
        """)
        
        if st.button("대화 내용 초기화"):
            st.session_state.message_list = []
            st.rerun()

def render_chat_messages():
    """
    채팅 메시지를 렌더링합니다.
    """
    for message in st.session_state.message_list:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def handle_user_input():
    """
    사용자 입력을 처리합니다.
    """
    if user_question := st.chat_input(placeholder="2025 공공기관 채용에 대해 궁금한 내용을 질문해주세요!"):
        # 사용자 메시지 표시
        with st.chat_message("user"):
            st.write(user_question)
        st.session_state.message_list.append({"role": "user", "content": user_question})

        # AI 응답 생성 및 표시
        with st.chat_message("ai"):
            message_placeholder = st.empty()
            full_response = ""
            
            # 초기 로딩 메시지 표시
            with st.spinner("정보를 검색하고 있습니다..."):
                # 첫 번째 청크를 받을 때까지 대기
                first_chunk = next(get_ai_response(user_question), None)
                if first_chunk:
                    full_response = first_chunk
                    message_placeholder.markdown(full_response + "▌")
            
            # 나머지 응답 스트리밍
            for chunk in get_ai_response(user_question):
                full_response += chunk
                message_placeholder.markdown(full_response + "▌")
            
            # 최종 응답 저장
            message_placeholder.markdown(full_response)
            st.session_state.message_list.append({"role": "ai", "content": full_response})

def main():
    """
    메인 애플리케이션을 실행합니다.
    """
    # 페이지 설정
    st.set_page_config(
        page_title="공공기관 채용정보 어시스턴트",
        page_icon="🤖",
        layout="wide"
    )

    # 제목 및 설명
    st.title("🤖 공공기관 채용 정보 어시스턴트")
    st.caption("2025년도의 공공기관 채용 정보에 대해 알려드립니다!")

    # 세션 상태 초기화
    init_session_state()

    # 사이드바 렌더링
    render_sidebar()

    # 채팅 메시지 렌더링
    render_chat_messages()

    # 사용자 입력 처리
    handle_user_input()

if __name__ == "__main__":
    main()
