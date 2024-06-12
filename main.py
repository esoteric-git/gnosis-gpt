import os
import tempfile
import streamlit as st
from files import file_uploader, url_uploader
from question import chat_with_doc
from gnosis import gnosis
from langchain.embeddings.openai import OpenAIEmbeddings
from stats import get_usage_today
from chroma_db import create_chroma_client, create_chroma_collection
import sidebar as sb
from explorer import view_document

# Initialize Chroma DB client and collection
chroma_client = create_chroma_client()
collection_name = "documents"
collection = create_chroma_collection(chroma_client, collection_name)

openai_api_key = st.secrets.openai_api_key
anthropic_api_key = st.secrets.anthropic_api_key
self_hosted = st.secrets.self_hosted

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
models = ["gpt-3.5-turbo", "gpt-4"]

# Set the theme
st.set_page_config(
    page_title="GnosisGPT",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize Sidebar
sb.sidebar(chroma_client, collection)

st.title("Gnosis GPT")
st.markdown("Store knowledge and chat with it.")
if self_hosted == "false":
    st.markdown('Self hosting message...')

st.markdown("---\n\n")

st.session_state["overused"] = False
if self_hosted == "false":
    usage = get_usage_today(chroma_client)  # Updated to use Chroma DB
    if usage > st.secrets.usage_limit:
        st.markdown(
            f"<span style='color:red'>You have used {usage} tokens today, which is more than your daily limit of {st.secrets.usage_limit} tokens.</span>", unsafe_allow_html=True)
        st.session_state["overused"] = True
    else:
        st.markdown(f"<span style='color:blue'>Usage today: {usage} tokens</span>", unsafe_allow_html=True)

# Create a radio button for user to choose between adding knowledge or asking a question
user_choice = st.radio(
    "Choose an action", ('Add Knowledge', 'Chat with Gnosis', 'Forget', "Explore"))

st.markdown("---\n\n")

if user_choice == 'Add Knowledge':
    # Display chunk size and overlap selection only when adding knowledge
    st.sidebar.title("Configuration")
    st.sidebar.markdown(
        "Choose your chunk size and overlap for adding knowledge.")
    st.session_state['chunk_size'] = st.sidebar.slider(
        "Select Chunk Size", 100, 1000, st.session_state['chunk_size'], 50)
    st.session_state['chunk_overlap'] = st.sidebar.slider(
        "Select Chunk Overlap", 0, 100, st.session_state['chunk_overlap'], 10)
    
    # Create two columns for the file uploader and URL uploader
    col1, col2 = st.columns(2)
    
    with col1:
        file_uploader(chroma_client, collection)
    with col2:
        url_uploader(chroma_client, collection)
elif user_choice == 'Gnosis Chat':
    # Display model and temperature selection only when asking questions
    st.sidebar.title("Configuration")
    st.sidebar.markdown(
        "Choose your model and temp.")
    if self_hosted != "false":
        st.session_state['model'] = st.sidebar.selectbox(
        "Select Model", models, index=(models).index(st.session_state['model']))
    else:
        st.sidebar.write("**Model**: gpt-3.5-turbo")
        st.sidebar.write("**Self Host")
        st.session_state['model'] = "gpt-3.5-turbo"
    st.session_state['temperature'] = st.sidebar.slider(
        "Select Temperature", 0.0, 1.0, st.session_state['temperature'], 0.1)
    if st.secrets.self_hosted != "false":
        st.session_state['max_tokens'] = st.sidebar.slider(
            "Select Max Tokens", 256, 2048, st.session_state['max_tokens'], 2048)
    else:
        st.session_state['max_tokens'] = 256
    
    chat_with_doc(st.session_state['model'], collection, stats_db=chroma_client)
elif user_choice == 'Forget':
    st.sidebar.title("Configuration")

    gnosis(chroma_client)
elif user_choice == 'Explore':
    st.sidebar.title("Configuration")
    view_document(collection)

st.markdown("---\n\n")
