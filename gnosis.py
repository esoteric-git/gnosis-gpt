

import streamlit as st
from chroma_db import get_document

def gnosis(chroma_client):
    doc_id = st.text_input('Enter Document ID to forget:')
    if doc_id:
        # Retrieve and display the document before deleting
        document = get_document(chroma_client, doc_id)
        if document:
            st.write(document['content'])
            if st.button('Delete Document'):
                # Delete the document from Chroma DB
                chroma_client.collection("documents").delete(doc_id)
                st.write('Document deleted.')
        else:
            st.write('Document not found.')
