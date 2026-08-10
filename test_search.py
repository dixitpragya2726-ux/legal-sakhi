import chromadb
from chromadb.utils import embedding_functions

# Connect to the same database you just built
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="legal_knowledge",
    embedding_function=embedding_fn
)

# Try a realistic question
query = "my colleague keeps sending me inappropriate messages at work"

results = collection.query(
    query_texts=[query],
    n_results=3   # get the top 3 most relevant chunks
)

print(f"Query: {query}\n")
for i, doc in enumerate(results["documents"][0]):
    source = results["metadatas"][0][i]["source"]
    print(f"--- Result {i+1} (from {source}) ---")
    print(doc)
    print()