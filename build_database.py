import os
import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step A: Read all .txt files from the legal-docs folder
def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
                documents.append({"filename": filename, "text": text})
    return documents

# Step B: Split each document into smaller chunks
def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    all_chunks = []
    for doc in documents:
        chunks = splitter.split_text(doc["text"])
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "id": f"{doc['filename']}_chunk_{i}",
                "source": doc["filename"],
                "text": chunk
            })
    return all_chunks

# Step C: Build the ChromaDB database
def build_database(chunks):
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(
        name="legal_knowledge",
        embedding_function=embedding_fn
    )

    collection.add(
        ids=[chunk["id"] for chunk in chunks],
        documents=[chunk["text"] for chunk in chunks],
        metadatas=[{"source": chunk["source"]} for chunk in chunks]
    )

    print(f"Successfully added {len(chunks)} chunks to ChromaDB")
    return collection

if __name__ == "__main__":
    docs = load_documents("legal-docs")
    print(f"Loaded {len(docs)} document(s)")

    chunks = chunk_documents(docs)
    print(f"Created {len(chunks)} chunks")

    build_database(chunks)