import chromadb

from documents import load_documents, chunk_text
from embeddings import create_embeddings


client = chromadb.PersistentClient(
    path="chroma_db"
)


collection = client.get_or_create_collection(
    name="rag_documents"
)


def build_vector_store():

    documents = load_documents()

    all_chunks = []
    metadatas = []
    ids = []

    chunk_id = 0

    for document in documents:

        chunks = chunk_text(document["text"])

        for chunk in chunks:

            all_chunks.append(chunk)

            metadatas.append({
                "source": document["filename"]
            })

            ids.append(f"chunk_{chunk_id}")

            chunk_id += 1

    embeddings = create_embeddings(all_chunks)

    collection.upsert(
        ids=ids,
        documents=all_chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(all_chunks)} chunks in ChromaDB.")


if __name__ == "__main__":

    build_vector_store()