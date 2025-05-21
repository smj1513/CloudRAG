from datetime import datetime
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

# 환경 변수 로드
load_dotenv()

# 현재 날짜 설정
today = datetime.today().strftime('%Y-%m-%d')

# 프롬프트 템플릿 설정
prompt = ChatPromptTemplate([
    ("system", f"You are a helpful AI assistant"),
    ("system", "반드시 출처를 표기해주세요."),
    ("system", f"Today's date is {today}"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
]) 