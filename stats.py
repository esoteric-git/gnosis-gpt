import sqlite3

def get_usage_today(chroma_client):
    # Example function to get usage stats from Chroma DB
    usage = 0
    # Retrieve and calculate usage from Chroma DB
    return usage

def add_usage(stats_db, action_type, details, metadata):
    # Add usage record to stats table in Chroma DB
    with stats_db.connect() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO stats (time, chat, embedding, details, metadata)
            VALUES (CURRENT_TIMESTAMP, ?, ?, ?, ?)
        """, (action_type == "chat", action_type == "embedding", details, metadata))
        conn.commit()
