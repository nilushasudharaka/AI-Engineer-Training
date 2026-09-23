import chromadb

from data.documents import documents
from embeddings import model


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="ai_knowledge"
)


texts = [document["text"] for document in documents]

ids = [document["id"] for document in documents]

metadatas = [
    {
        "topic": document["topic"],
        "category": document["category"]
    }
    for document in documents
]


embeddings = model.encode(texts).tolist()


collection.upsert(
    ids=ids,
    documents=texts,
    embeddings=embeddings,
    metadatas=metadatas
)


print("Documents stored successfully.")
print("Number of documents:", collection.count())