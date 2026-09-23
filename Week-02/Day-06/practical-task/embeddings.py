from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):
    return model.encode(text).tolist()


if __name__ == "__main__":
    text = "Machine learning learns patterns from data."

    embedding = create_embedding(text)

    print("Text:")
    print(text)

    print("\nEmbedding:")
    print(embedding)

    print("\nVector dimensions:")
    print(len(embedding))