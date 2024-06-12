import chromadb
from chromadb.config import Settings

def create_chroma_client():
    settings = Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=".chroma"  # You can customize this directory
    )
    client = chromadb.Client(settings)
    return client

def create_chroma_collection(client, collection_name):
    collection = client.create_collection(name=collection_name)
    return collection

def add_document(collection, document_id, content, metadata, embedding):
    collection.add(
        documents=[{
            "id": document_id,
            "content": content,
            "metadata": metadata,
            "embedding": embedding
        }]
    )

def get_document(collection, document_id):
    return collection.get(id=document_id)

def query_collection(collection, query_embedding, top_k=10):
    results = collection.query(query_embedding=query_embedding, n_results=top_k)
    return results
