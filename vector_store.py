# vector_store.py
import chromadb
from chromadb.utils import embedding_functions

# Initialize ChromaDB in-memory client
client = chromadb.Client()
collection = client.get_or_create_collection("marketing_best_practices")

# Add sample data (only done once in memory session)
collection.add(
    documents=[
        "Use emojis and call-to-actions for Instagram.",
        "Maintain professionalism and clarity on LinkedIn.",
        "Short, witty phrases with hashtags work best on Twitter.",
        "Facebook ads do well with emotional appeal and storytelling."
    ],
    metadatas=[
        {"tone": "fun", "platform": "Instagram"},
        {"tone": "professional", "platform": "LinkedIn"},
        {"tone": "witty", "platform": "Twitter"},
        {"tone": "fun", "platform": "Facebook"}
    ],
    ids=["1", "2", "3", "4"]
)

def get_best_practices(tone, platform):
    results = collection.query(
        query_texts=[f"{tone} tone {platform} ad copy best practices"],
        n_results=1
    )
    return results["documents"][0][0] if results["documents"] else "No best practices found."
