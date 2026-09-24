import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from retriever import retrieve_documents


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


MODEL_NAME = "gemini-3.5-flash-lite"


def generate_answer(question):

    # Retrieve relevant document chunks
    documents, metadatas = retrieve_documents(question)

    # Build context
    context_parts = []

    for document, metadata in zip(documents, metadatas):

        context_parts.append(
            f"Source: {metadata['source']}\n"
            f"{document}"
        )

    context = "\n\n".join(context_parts)

    # Create RAG prompt
    prompt = f"""
You are a helpful question-answering assistant.

Answer the user's question using ONLY the provided context.

Do not use outside knowledge.

If the answer cannot be found in the provided context,
say:

"I could not find the answer in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate answer using Gemini
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
        ),
    )

    return response.text, context