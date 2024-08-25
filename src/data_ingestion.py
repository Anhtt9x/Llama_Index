import logging
from llama_index.core import SimpleDirectoryReader
import sys


def load_data(data_path):
    try:
        logging.info("Data starting loaded...")

        data = SimpleDirectoryReader(data_path)

        documents = data.load_data()
        
        logging.info("Data loading completed...")
        return documents
    
    except Exception as e:
        logging.info("Exception...")
        raise e
