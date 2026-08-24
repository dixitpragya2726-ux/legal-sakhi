import os
from dotenv import load_dotenv
import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions

# Load your API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.5-flash")

# Connect to your existing ChromaDB database
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(
    name="legal_knowledge",
    embedding_function=embedding_fn
)

def retrieve_relevant_chunks(query, n_results=5):
    """Search ChromaDB for the most relevant legal chunks."""
    results = collection.query(query_texts=[query], n_results=n_results)
    chunks = results["documents"][0]
    sources = [meta["source"] for meta in results["metadatas"][0]]
    return chunks, sources

def generate_answer(user_query):
    """Retrieve relevant law, then ask Gemini to explain it simply."""
    chunks, sources = retrieve_relevant_chunks(user_query)
    legal_context = "\n\n".join(chunks)

    prompt = f"""You are a compassionate legal assistant helping women in India understand their rights after facing harassment, assault, or abuse.

Rules you must follow:
- Only use the legal information provided below - do not make up laws or sections
- Explain things in simple, warm, plain language - no legal jargon
- Be supportive and non-judgmental in tone
- If the context doesn't clearly answer the question, say so honestly rather than guessing
- End by reminding them this is guidance, not a substitute for a real lawyer

Relevant legal information:
{legal_context}

The person's situation: {user_query}

Please explain in simple language what law applies here and what it means for them."""

    response = model.generate_content(prompt)
    answer = response.text
    return answer, sources

# Test it
if __name__ == "__main__":
    query = "my manager asked for favours to get promrtions and also meesages me frequently at late night "
    answer, sources = generate_answer(query)

    print(f"Question: {query}\n")
    print(f"Answer:\n{answer}\n")
    print(f"Sources used: {', '.join(set(sources))}")

def get_helplines():
    return [
        {"name": "Women Helpline", "number": "181"},
        {"name": "Police Helpline", "number": "1091"},
        {"name": "Emergency", "number": "112"},
        {"name": "Childline", "number": "1098"},
        {"name": "Cyber Crime Helpline", "number": "1930"}
    ]

def draft_complaint(user_query):
    chunks, sources = retrieve_relevant_chunks(user_query)
    legal_context = "\n\n".join(chunks)

    prompt = f"""Based on this situation: {user_query}

And this relevant law:
{legal_context}

Draft a formal, ready-to-file complaint letter. Include: complainant details as placeholders [Your Name], [Address], [Date], incident description based on what was shared, the relevant law cited, and a formal closing. Keep it professional and clear."""

    response = model.generate_content(prompt)
    return response.text, sources

def get_evidence_checklist():
    return [
        "Do not delete messages, chats, or emails",
        "Take screenshots with date and time visible",
        "Save call logs and recordings if any",
        "Note down witness details if anyone saw or knows about the incident",
        "Write down what happened as soon as possible, with dates and times, while it's fresh in memory",
        "Report as early as possible to the relevant authority"
    ]