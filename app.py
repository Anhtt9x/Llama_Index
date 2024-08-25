from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.llms.gemini import Gemini
from IPython.display import Markdown
from llama_index.core import Settings, StorageContext, load_index_from_storage,ServiceContext
import google.generativeai as genai
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os

load_dotenv()


google_api_key = os.getenv("GOOGLE_API_KEY")


data = SimpleDirectoryReader("data")

documents = data.load_data()

gemini=Gemini(model="models/gemini-1.5-pro",api_key=google_api_key)

Settings.llm = gemini

Settings.embed_model = GeminiEmbedding(model_name="models/text-embedding-004",api_key=google_api_key)

Settings.node_parser = SentenceSplitter(chunk_size=500,chunk_overlap=20)


index = VectorStoreIndex.from_documents(documents=documents)

index.storage_context.persist("storage")

engine = index.as_query_engine()

response = engine.query("what is RAG domain ?")
print(response.response)

