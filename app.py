import streamlit as st

st.set_page_config(
    page_title="AI Personal Study Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Personal Study Assistant")

st.write("Welcome! Your AI-powered study assistant is ready.")

st.info("Upload your study material and ask questions from your notes.")

uploaded_file = st.file_uploader(
    "📄 Upload your study material",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

question = st.text_input(
    "💬 Ask a question"
)

if st.button("Ask AI"):
    if question:
        st.write("Your question:", question)
        st.warning("AI/RAG functionality will be connected in the next step.")
    else:
        st.warning("Please enter a question.")

