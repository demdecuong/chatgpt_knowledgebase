import os
import openai
import time
from langchain.chains import VectorDBQA
from langchain.chat_models import ChatOpenAI


from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders.unstructured import UnstructuredFileLoader 
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

openai_api_key = os.geteenv('OPENAI_API_KEY')
loader = UnstructuredFileLoader('document.txt')

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

db = Chroma.from_documents(texts, embeddings)


qa = VectorDBQA.from_chain_type(llm=ChatOpenAI(), chain_type="stuff", vectorstore=db, k=1)
query = "Sản phẩm này có những gì cần lưu ý"
out = qa.run(query)
print(out)