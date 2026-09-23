import chromadb

from embeddings import model


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="ai_knowledge"
)


query = "How can computers learn from data?"

query_embedding = model.encode(query).tolist()


results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)


print("\nQuery:")
print(query)

print("\nMost Similar Documents:")

for i, document in enumerate(results["documents"][0]):
    distance = results["distances"][0][i]

    print("\nResult", i + 1)
    print("Document:", document)
    print("Distance:", distance)