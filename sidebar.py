import streamlit as st
from chroma_db import get_document

def sidebar(chroma_client, collection):
    st.sidebar.title("Database Information") 
    number_of_docs = number_of_documents(collection)
    st.sidebar.markdown(f"**Docs in DB:**  {number_of_docs}")

def number_of_documents(collection):
    # Assuming collection has a method to count documents
    documents = collection.get()
    return len(documents)
