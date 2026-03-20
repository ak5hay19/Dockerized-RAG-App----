
# IMPORTS

from langchain_groq import ChatGroq
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser

# API KEY loading

import os
from dotenv import load_dotenv
load_dotenv()

# Load Text doc

loader = TextLoader("data.txt")
documents = loader.load()

# Split the doc into chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n","\n","  "])  
docs = text_splitter.split_documents(documents)

# Create embeddings

embeddings = embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vectorstore

vectorstore = FAISS.from_documents(docs, embeddings)

# Create Retriever

retriever = vectorstore.as_retriever()

# Create LLM

llm = ChatGroq(model = "llama-3.1-8b-instant")

# Create Prompt Templates

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant for answering questions about the document provided. Use only the following retrieved information to answer the question.
 If you don't know the answer, say you don't know.
 Context: {context}
 Question: {query}
    """
)

# Start the conversation( Q-A loop)

print("RAG app ready, Type 'exit' to quit")

while True:
    query = input("Query: ")
    if query.lower() == "exit":
        print("Exiting the RAG app. Goodbye!")
        break

    # Retrieve relevant documents

    retrieved_docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    # Build Chain

    chain = prompt | llm | StrOutputParser()

    # Get Responsee

    response = chain.invoke({"context": context, "query": query})
    print("Answer:", response)
    print("\n"+"-"*69+"\n")