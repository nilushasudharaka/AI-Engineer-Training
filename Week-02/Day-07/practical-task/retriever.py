from vector_store import collection
from embeddings import create_embeddings


def retrieve_documents(question, number_of_results=3):

    question_embedding = create_embeddings(
        [question]
    )[0]

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=number_of_results
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return documents, metadatas


if __name__ == "__main__":

    question = input("Enter your question: ")

    documents, metadatas = retrieve_documents(question)

    print("\nRetrieved Context:\n")

    for i, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1
    ):

        print(f"--- Result {i} ---")
        print(f"Source: {metadata['source']}")
        print(document)
        print()