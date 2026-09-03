import os
import json
import math
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


def generate_answer(user_query, language="en"):
    """Retrieve relevant law, then ask Gemini to explain it simply, in the requested language."""

    if not user_query or not user_query.strip():
        if language == "hi":
            return (
                "ऐसा लगता है कि आपका संदेश खाली था। कृपया अपना प्रश्न लिखें या बताएं कि क्या हो रहा है, "
                "और मैं आपकी मदद करने की पूरी कोशिश करूंगी।",
                []
            )
        return (
            "It looks like your message was empty. Please type your question or "
            "describe what's happening, and I'll do my best to help.",
            []
        )

    trivial_greetings = {"hi", "hii", "hiii", "hello", "hey", "yo", "sup", "hola", "namaste", "namaskar"}
    normalized = user_query.strip().lower().strip("!.,? ")

    if normalized in trivial_greetings or len(normalized) <= 2:
        if language == "hi":
            return (
                "नमस्ते! मैं आपके लिए एक सुरक्षित, सहयोगी स्थान प्रदान करने के लिए यहाँ हूँ। यह सहायक विशेष रूप से "
                "उन महिलाओं के लिए कानूनी जानकारी और सुरक्षा सहायता प्रदान करने पर केंद्रित है जो उत्पीड़न, हमले, या "
                "दुर्व्यवहार का सामना कर रही हैं। यदि आप किसी कठिन परिस्थिति से गुज़र रही हैं, या आपका कोई विशिष्ट "
                "कानूनी प्रश्न है, तो कृपया बेझिझक साझा करें।\n\n"
                "*कृपया याद रखें कि यह जानकारी केवल मार्गदर्शन के लिए है, और यह किसी वास्तविक वकील की पेशेवर "
                "सलाह का विकल्प नहीं है।*",
                []
            )
        return (
            "Hello! I am here to offer a safe, supportive space for you. This assistant "
            "is focused on providing legal information and safety support for women who may "
            "be facing harassment, assault, or abuse. If you're going through a difficult "
            "situation, or have a specific legal question, please feel free to share whatever "
            "you feel comfortable with.\n\n"
            "*Please remember that this is guidance, not a substitute for professional legal advice from a real lawyer.*",
            []
        )

    chunks, sources = retrieve_relevant_chunks(user_query)
    legal_context = "\n\n".join(chunks)

    language_instruction = (
        "IMPORTANT: Respond entirely in Hindi (Devanagari script), in a warm, simple, natural tone — "
        "as if speaking to someone directly, not a literal word-for-word translation. The legal information "
        "provided below is in English; read and understand it, then explain it fully in Hindi."
        if language == "hi"
        else "Respond in English."
    )

    prompt = f"""You are a compassionate legal assistant helping women in India understand their rights after facing harassment, assault, or abuse.

Rules you must follow:
- Only use the legal information provided below - do not make up laws or sections
- Explain things in simple, warm, plain language - no legal jargon
- Be supportive and non-judgmental in tone
- If the context doesn't clearly answer the question, say so honestly rather than guessing
- End by reminding them this is guidance, not a substitute for a real lawyer
- If the person's message is a greeting, a random/unrelated question with no connection to legal help, safety, or personal incidents, or otherwise not something you can meaningfully answer using the legal information below, do NOT force a legal explanation. Instead, gently let them know this assistant is focused on legal and safety support, and invite them to share what's going on or ask a legal question.
- {language_instruction}

Relevant legal information:
{legal_context}

The person's situation: {user_query}

Please explain in simple language what law applies here and what it means for them. If their message isn't related to legal or safety support, follow the rule above instead."""

    response = model.generate_content(prompt)
    answer = response.text
    return answer, sources



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


def haversine_distance_km(lat1, lon1, lat2, lon2):
    """Calculate great-circle distance between two lat/long points, in kilometers."""
    R = 6371  # Earth's radius in km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2) ** 2
         + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def get_nearby_centers(search_term="", user_lat=None, user_lng=None):
    """
    Return nearby centers. If user_lat/user_lng are provided, sort all centers
    that have coordinates by real distance. Otherwise, fall back to text search
    by city/state/name.
    """
    with open("legal_aid_centers.json", "r", encoding="utf-8") as f:
        centers = json.load(f)

    # If we have the user's real coordinates, calculate distance for every
    # center that has lat/lng, and sort nearest-first.
    if user_lat is not None and user_lng is not None:
        centers_with_coords = []
        centers_without_coords = []

        for c in centers:
            if c.get("latitude") is not None and c.get("longitude") is not None:
                distance = haversine_distance_km(
                    user_lat, user_lng, c["latitude"], c["longitude"]
                )
                c_copy = dict(c)
                c_copy["distance_km"] = round(distance, 2)
                centers_with_coords.append(c_copy)
            else:
                centers_without_coords.append(c)

        centers_with_coords.sort(key=lambda c: c["distance_km"])

        # If a city/search term was also given, narrow down by it first
        if search_term:
            term = search_term.lower()
            centers_with_coords = [
                c for c in centers_with_coords
                if term in c.get("address", "").lower()
                or term in c.get("scope", "").lower()
                or term in c.get("name", "").lower()
            ]

        return centers_with_coords if centers_with_coords else centers

    # Fallback: no coordinates provided, use the original text search
    if not search_term:
        return centers

    search_term = search_term.lower()
    matching = [
        c for c in centers
        if search_term in c.get("address", "").lower()
        or search_term in c.get("scope", "").lower()
        or search_term in c.get("name", "").lower()
    ]
    return matching if matching else centers


# Test it
if __name__ == "__main__":
    query = "my manager asked for favours to get promotions and also messages me frequently at late night"
    answer, sources = generate_answer(query)

    print(f"Question: {query}\n")
    print(f"Answer:\n{answer}\n")
    print(f"Sources used: {', '.join(set(sources))}")