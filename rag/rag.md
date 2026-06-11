# rag

## 1. 基本概念

1. Document Loader: 将各种数据转换为文本数据，如pdf，网页等
2. Chunk: 切块。文档太长，不能整篇塞给大模型，所以要切成小段。
3. Embedding: 把文字变成向量
4. Vector Store: 向量数据库。用来存 embedding。
5. Retriever: 检索器。用户提问后，从向量数据库里找最相关的内容。
6. Prompt: 把检索到的资料和用户问题拼起来