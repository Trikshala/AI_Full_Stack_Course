from ollama import chat
import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

system_msg = "You are Nova, a friendly Technova fest concierge. Answer ONLY using the context provided. If the context does not contain the answer, say you don't have that information. Keep answers short."
MIN_SCORE = 0.3

st.set_page_config(page_title = "Fest Concierge", page_icon="🎪", layout="wide")

@st.cache_resource
def load_resources():
    model = SentenceTransformer('all-MiniLM-L6-V2')
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection("fest_docs")
    return model, collection

model, collection = load_resources()

st.title("🎪 Nova, the Technova Concierge")
st.caption("I only know what's in the fest documents. Ask me anything about Technova!")

with st.sidebar:
    st.header("Settings")
    top_k = st.slider("Chunks to retrieve (top-k)", 1,5,3)
    st.divider()

st.session_state.setdefault("last_query", "-")
st.session_state.setdefault("results", [])
st.session_state.setdefault("answer", "")
st.session_state.setdefault("recent", [])

def retrieve(question, k=3):
    q_emb = model.encode(question).tolist()
    res = collection.query(query_embeddings=[q_emb], n_results=k)
    return list(zip(res["ids"][0], res["documents"][0], res["distances"][0]))

def to_similarity(dist):
    return max(0.0, 1 - dist/2)

def badge(score):
    if score >= 0.5:
        return "🟢"
    if score >= 0.3:
        return "🟡"
    return "🔴"

def ask_llama(question, results):
    context = "\n\n".join(text for _, text, _ in results)
    messages = [{"role":"system", "content" : system_msg},
                {"role" : "user", "content":f"Context:\n{context}\n\nQuestion: {question}"}]
    response = chat(model = "llama3.2", messages = messages)
    return response.message.content

left, right = st.columns(2)

with left:
    st.subheader("💬 Ask Nova")
    question = st.text_input("Your question", placeholder="When does the hackathon start?")
    search = st.button("🔍 Search")

if search and question:
    st.session_state.last_query = question
    st.session_state.results = retrieve(question, top_k)
    if question in st.session_state.recent:
        st.session_state.recent.remove(question)
    st.session_state.recent.insert(0, question)
    st.session_state.recent = st.session_state.recent[:5]

with right:
    st.subheader("📌 Evidence")
    if not st.session_state.results:
        st.info("Retrieved chunks will appear here.")
    for chunk_id, text, dist in st.session_state.results:
        score = to_similarity(dist)
        st.warning(f"**📌 {chunk_id}** {badge(score)} match {score: .0%}\n\n{text}")

with left:
    if search and question:
        results = st.session_state.results
        if to_similarity(results[0][2]) < MIN_SCORE:
            st.session_state.answer = "I couldn't find anything about that in the fest documents. Try rephrasing the question!"
        else:
            try:
                with st.spinner("Nova is reading the notes..."):
                    st.session_state.answer = ask_llama(question, results)
            except Exception as e:
                st.session_state.answer = ""
                st.error("Something went wrong. Is ollama running?")
    if st.session_state.answer:
        st.markdown("### Nova says")
        st.write(st.session_state.answer)

with st.sidebar:
    st.header("🧠 Knowledge meter")
    st.metric("Chunks in memory", collection.count())
    st.caption("Last searched topic")
    st.write(st.session_state.last_query)
    st.divider()
    st.subheader("🕘 Recent searches")
    for q in st.session_state.recent:
        st.write(f"• {q}")