import streamlit as st
from chroma_db import add_document
from chroma_db import get_document

def view_document(collection):
    # Get the documents from the database
    response = collection.get()
    st.write("**This feature is in active development**")
    # Display a list of elements from the documents
    # If the user clicks on an element, display the content of the document
    for document in response:
        if st.button(document['content'][:50].replace("\n", " ")):
            st.write(document['content'])


def file_uploader(chroma_client, collection):
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            # Process the file and add its content to Chroma DB
            document_id = uploaded_file.name
            content = bytes_data.decode('utf-8')  # Assuming text content
            metadata = {}  # Add any relevant metadata
            embedding = []  # Generate embedding using OpenAIEmbeddings or any other method
            add_document(collection, document_id, content, metadata, embedding)
