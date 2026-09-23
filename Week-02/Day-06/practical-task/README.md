# Day 6 - Embeddings & Vector Databases

## Objective

Build a small semantic search system using text embeddings
and ChromaDB.

## Technologies

- Python
- Sentence Transformers
- ChromaDB

## Concept Flow

Text
↓
Embedding Model
↓
Vector
↓
ChromaDB
↓
Similarity Search
↓
Relevant Documents

## What I Implemented

1. Created a small collection of text documents.
2. Converted the documents into embeddings.
3. Stored the embeddings in ChromaDB.
4. Added metadata to each document.
5. Implemented similarity search.
6. Built an interactive semantic search application.
7. Tested different queries.
8. Documented limitations.

## Results

The system was able to retrieve semantically related
documents even when the query did not use exactly the
same wording as the stored document.

## Limitations

- The dataset contains only a small number of documents.
- The system may return a related document even when the
  correct answer is not present.
- Similarity does not guarantee factual correctness.
- Search quality depends on the embedding model.
- No reranking or similarity threshold was implemented.

## Conclusion

This practical task demonstrated how text can be converted
into vector representations and stored in a vector database
for semantic similarity search.