from pathlib import Path


DATA_FOLDER = Path("data")


def load_documents():
    documents = []

    for file_path in DATA_FOLDER.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "filename": file_path.name,
            "text": text
        })

    return documents


def chunk_text(text, chunk_size=300):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk.strip())

    return chunks


if __name__ == "__main__":

    documents = load_documents()

    for document in documents:

        chunks = chunk_text(document["text"])

        print(f"\nDocument: {document['filename']}")
        print(f"Number of chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks):

            print(f"\nChunk {i + 1}:")
            print(chunk)