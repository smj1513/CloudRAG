from typing import List
from langchain_core.tools import tool
from langchain_core.documents import Document
from langchain_community.tools import TavilySearchResults
from langchain_community.vectorstores import FAISS, DistanceStrategy
from langchain_openai import OpenAIEmbeddings

# 임베딩 모델 초기화
embedding = OpenAIEmbeddings(model="text-embedding-3-small")

# 벡터 스토어 로드
vector_store = FAISS.load_local(
    './embedding_vectors',
    index_name='public_enterprise',
    embeddings=embedding,
    allow_dangerous_deserialization=True,
    distance_strategy=DistanceStrategy.COSINE
)

# 검색 도구 설정
search_tool = TavilySearchResults(
    max_result=5,
    search_depth="advanced"
)

@tool
def search_info(query: str) -> List[Document]:
    """
    공공기관 채용 정보와 관련하여 정보가 필요할 때는 이 도구를 참조하세요.
    """
    docs = vector_store.similarity_search(query, k=4)
    if len(docs) > 0:
        return docs
    return [Document(page_content="관련 정보를 찾을 수 없습니다.")]

# 사용 가능한 도구 목록
tools = [search_tool, search_info] 