from llama_index.core import SimpleDirectoryReader,VectorStoreIndex
from llama_index.llms.gemini import Gemini
from IPython.display import Markdown
from llama_index.core import ServiceContext, StorageContext, load_index_from_storage
import google.generativeai as genai
from llama_index.embeddings.gemini import GeminiEmbedding
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

data = SimpleDirectoryReader("data")

documents = data.load_data()

model = genai.GenerativeModel("gemini-1.5-pro")

embedding = GeminiEmbedding(model_name="models/text-embedding-004")

service_context = ServiceContext.from_defaults(llm=model, embed_model=embedding,chunk_size=800,chunk_overlap=200)

index = VectorStoreIndex.from_documents(documents=documents,service_context=service_context)

