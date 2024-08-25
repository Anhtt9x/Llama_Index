import logging
import os
import sys
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')

def load_model():
    try:
        logging.info("Model prepare to load...")

        model = Gemini(api_key=google_api_key,model_name="models/gemini-1.5-pro")

        return model

    except Exception as e:
        logging.info("Model didn't downloaded")
        raise e
    