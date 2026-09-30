import os
import faiss
import numpy as np

from app.embeddings import create_chunks, create_embeddings


VECTOR_DB_PATH = "vector_db/index.faiss"
CHUNKS_PATH = "vector_db/chunks.npy"


def create_vector_database(text):
    chunks = create_chunks(text)

    if not chunks:
        raise ValueError("No text found in document.")

    embeddings = create_embeddings(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

    os.makedirs("vector_db", exist_ok=True)

    faiss.write_index(index, VECTOR_DB_PATH)
    np.save(CHUNKS_PATH, np.array(chunks, dtype=object))

    return len(chunks)


def search_similar_chunks(query, top_k=3):
    index = faiss.read_index(VECTOR_DB_PATH)

    chunks = np.load(
        CHUNKS_PATH,
        allow_pickle=True
    )

    query_embedding = create_embeddings([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    results = []

    for i in indices[0]:
        if i < len(chunks):
            results.append(chunks[i])

    return results