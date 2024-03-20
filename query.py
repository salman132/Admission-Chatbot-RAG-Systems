import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain import hub

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = PineconeVectorStore(
    index_name="collegeinfo", embedding=embeddings_model
)
retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 15})
combine_docs_chain = create_stuff_documents_chain(
    llm, retrieval_qa_chat_prompt
)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
question = input("Please ask your query here: ")
print(retrieval_chain.invoke({"input": question})["answer"])