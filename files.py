# files.py

import streamlit as st
from chroma_db import add_document

def file_uploader(chroma_client, collection):
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            # Here, process the file and add its content to Chroma DB
            document_id = uploaded_file.name
            content = bytes_data.decode('utf-8')  # Assuming text content
            metadata = {}  # Add any relevant metadata
            embedding = []  # Generate embedding using OpenAIEmbeddings or any other method
            add_document(collection, document_id, content, metadata, embedding)

def url_uploader(chroma_client, collection):
    url = st.text_input('Enter URL')
    if url:
        # Here, fetch the URL content and add it to Chroma DB
        document_id = url
        content = ""  # Fetch and process the URL content
        metadata = {"url": url}
        embedding = []  # Generate embedding using OpenAIEmbeddings or any other method
        add_document(collection, document_id, content, metadata, embedding)
        st.write(f"Added document from URL: {url}")
