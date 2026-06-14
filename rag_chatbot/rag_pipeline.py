from groq import Groq

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from rag_chatbot.config import GROQ_API_KEY


# Groq Client
client = Groq(api_key=GROQ_API_KEY)

# Embedding Model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load ChromaDB
db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding
)

print("Collection Count:", db._collection.count())

# Retriever
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)


def ask_question(question):

    try:

        # Retrieve documents
        docs = retriever.invoke(question)

        print("\n===== RETRIEVED DOCUMENTS =====")
        print(f"Retrieved {len(docs)} documents")

        for i, doc in enumerate(docs):
            print(f"\n----- DOCUMENT {i+1} -----")
            print(doc.page_content[:500])

        # Create context
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are an AI Insurance Assistant for Acko Insurance.

Answer ONLY using the provided context.

Rules:
- Use simple English.
- Keep answers concise.
- Use bullet points when useful.
- Do not make up information.
- If the answer is not found in the context, say:
"Sorry, I could not find that information in the policy documents."

Context:
{context}

Question:
{question}
"""

        # Groq Response
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)
        return f"Error: {str(e)}"