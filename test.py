from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate

from langchain.chains.retrieval_qa.base import RetrievalQA
import chromadb
from langchain.memory import ConversationBufferMemory
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory




chat_message_history = MongoDBChatMessageHistory(
    session_id="test_session",
    connection_string="mongodb://root:password@:27017",
    database_name="history_db",
    collection_name="chat_histories",
)



client = chromadb.HttpClient(host="localhost", port=8000)
# # print(client)
embeddings = OllamaEmbeddings(base_url= 'http://localhost:11434/', model='all-minilm')
llm = Ollama(base_url= 'http://localhost:11434/', model='llama2')
# # print(llm.invoke('hi'))
text_splitter = RecursiveCharacterTextSplitter()
loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
doc = loader.load()
splitted_docs = text_splitter.split_documents(doc)
# # # print(splitted_docs[0])
vecdb = Chroma.from_documents(documents=splitted_docs, embedding=embeddings, persist_directory='.\chroma\db')

template = """
Use the following context (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the question:
------
<ctx>
{context}
</ctx>
------
<hs>
{history}
</hs>
------
{question}
Answer:
"""
prompt = PromptTemplate(
    input_variables=["history", "context", "question"],
    template=template,
)
memory = ConversationBufferMemory(
    chat_memory= chat_message_history,
    memory_key="history",
    input_key="question"
)

retrieval_chain = RetrievalQA.from_chain_type(llm,
                                              chain_type='stuff',
                                              retriever=vecdb.as_retriever(),
                                              chain_type_kwargs={
                                                  "prompt": prompt,
                                                  "memory": memory
                                              })


while True:
    query = input("enter your query: ")
    if query == 'ok bye':
        break
    else:
        response = retrieval_chain.invoke(query)
        print(response['result'])

