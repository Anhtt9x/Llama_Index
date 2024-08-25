import streamlit as st
from src.data_ingestion import load_data
from src.model_api import load_model
from src.embedding import embedding_data
import tempfile
import os

def main():
    st.set_page_config("QA with documents")

    st.header("QA with RAG documents")

    uploader = st.file_uploader("Upload your documents",type=["pdf","jpg"])

    inputs = st.text_input("Let's ask the model")

    if uploader is not None and inputs:
        with st.spinner("Model response..."):

            tmp_dir = tempfile.mkdtemp()

            tmp_file = os.path.join(tmp_dir,uploader.name)

            with open(tmp_file,"wb") as tmp:
                tmp.write(uploader.read())


            documents = load_data(tmp_dir)

            model = load_model()

            query_engine = embedding_data(model=model,documents=documents)

            response = query_engine.query(inputs).response

            st.write(response)

            st.success("Done")



if __name__ == "__main__":
    main()