from sentence_transformers import SentenceTransformer
import chromadb

with open("fest_info.txt", "r", encoding="utf-8") as f:
    text = f.read()

def chunk_text(text, chunk_size = 300, overlap = 50):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start+chunk_size])
        start += chunk_size - overlap
    return chunks

chunks = chunk_text(text)

model = SentenceTransformer("all-MiniLM-L6-V2")
embeddings = model.encode(chunks)

client = chromadb.PersistentClient(path = "chroma_db")
collection = client.get_or_create_collection(name="fest_docs")

collection.upsert(
    ids = [f"chunk_{i}" for i in range(len(chunks))],
    documents = chunks,
    embeddings = embeddings
)

print(f"Successfully stored {collection.count()} chunks in chromadb.")
