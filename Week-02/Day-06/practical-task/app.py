import chromadb
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="ai_knowledge"
)


print("=" * 60)
print("SEMANTIC SEARCH SYSTEM")
print("=" * 60)

while True:

    query = input("\nEnter your search query (or type 'exit'): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    print("\nMost Relevant Documents:")

    for i, document in enumerate(results["documents"][0]):

        print(f"\nResult {i + 1}")
        print("Document:", document)
        print("Topic:", results["metadatas"][0][i]["topic"])
        print("Category:", results["metadatas"][0][i]["category"])
        print("Distance:", results["distances"][0][i])