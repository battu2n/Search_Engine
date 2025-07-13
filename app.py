import streamlit as st
from search_engine import SemanticSearchEngine, load_documents
def load_documents(file_path):
    """Load documents from a text file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

st.title("Semantic Search Engine")

# Load and prepare
search_engine = SemanticSearchEngine()
documents = load_documents('faq.txt')
search_engine.add_documents(documents)

query = st.text_input("Search your question:")
top_k = st.slider("Number of results", 1, 5, 3)

if query:
    results = search_engine.search(query, top_k=top_k)
    if results:
        st.write(f"{top_k}Matches:")
        for result in results:
            st.write(f"(Score: {result['similarity']:.2f}")
            st.write(f"{result['document']}")
    else:
        st.write("No matches found.")