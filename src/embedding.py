from llama_index.core import VectorStoreIndex,Settings
from llama_index.embeddings.gemini import GeminiEmbedding
from src.data_ingestion import load_data
from src.model_api import load_model
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os
import logging

load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')

def embedding_data(model,documents):
    try:


        Settings.node_parser = SentenceSplitter(chunk_overlap=20, chunk_size=500)

        Settings.llm = model

        Settings.embed_model = GeminiEmbedding(api_key=google_api_key)

        index = VectorStoreIndex.from_documents(documents=documents)
        logging.info("Embed data success")

        index.storage_context.persist()

        query_engine = index.as_query_engine()
        logging.info("Model engine has ready")
        
        return query_engine
    
    except Exception as e:
        logging.info("error")
        raise e
    


        