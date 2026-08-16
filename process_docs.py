import os
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
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    all_chunks = []
    for doc in documents:
        chunks = splitter.split_text(doc["text"])
        for chunk in chunks:
            all_chunks.append({"source": doc["filename"], "text": chunk})
    return all_chunks

# Run it
if __name__ == "__main__":
    docs = load_documents("legal-docs")
    print(f"Loaded {len(docs)} document(s)")

    chunks = chunk_documents(docs)
    print(f"Created {len(chunks)} chunks\n")

    # Print the first 5 chunks so you can see what they look like
    for i, chunk in enumerate(chunks[:5]):
        print(f"--- Chunk {i+1} (from {chunk['source']}) ---")
        print(chunk["text"])
        print()