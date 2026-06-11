from openai import OpenAI
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb


# 1. 读取 .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")


# 2. 加载 embedding 模型
# 第一次运行会下载模型，可能比较慢
embedding_model = SentenceTransformer("BAAI/bge-small-zh-v1.5")


# 3. 创建 Chroma 客户端，数据会保存到 ./chroma_db
chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="rag_demo"
)


# 4. 读取本地 txt
def load_text(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# 5. 文本切块
def split_text(text: str, chunk_size: int = 10, overlap: int = 3) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start = end - overlap

    return chunks


# 6. 把文本转成向量
def embed_texts(texts: list[str]) -> list[list[float]]:
    embeddings = embedding_model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings.tolist()


# 7. 建立向量库
def build_vector_db(file_path: str = "data.txt"):
    text = load_text(file_path)
    chunks = split_text(text)

    ids = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f"chunk_{i}")
        metadatas.append({
            "source": file_path,
            "chunk_index": i
        })

    embeddings = embed_texts(chunks)

    # 避免重复添加：先删除旧 collection，再重建
    global collection
    try:
        chroma_client.delete_collection(name="rag_demo")
    except Exception:
        pass

    collection = chroma_client.get_or_create_collection(
        name="rag_demo"
    )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"向量库构建完成，共写入 {len(chunks)} 个文本块。")


# 8. 向量检索
def retrieve(question: str, top_k: int = 3) -> list[str]:
    question_embedding = embed_texts([question])[0]

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]

    return documents


# 9. 构造 Prompt
def build_prompt(question: str, contexts: list[str]) -> str:
    context_text = "\n\n".join(contexts)

    prompt = f"""
请只根据下面的资料回答问题。
如果资料中没有相关内容，请回答：资料中没有提到。

资料：
{context_text}

问题：
{question}
"""
    return prompt


# 10. 调用大模型
def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "你是一个严谨的知识库问答助手。"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# 11. 主程序
def main():
    build_vector_db("rag/data.txt")

    print("Chroma RAG 系统已启动。输入 exit 退出。")

    while True:
        question = input("\n你：")

        if question.strip().lower() == "exit":
            break

        contexts = retrieve(question, top_k=3)

        if not contexts:
            print("AI：资料中没有提到。")
            continue

        prompt = build_prompt(question, contexts)
        answer = ask_llm(prompt)

        print("\n检索到的资料：")
        for i, ctx in enumerate(contexts, 1):
            print(f"[{i}] {ctx}")

        print("\nAI：")
        print(answer)


if __name__ == "__main__":
    main()