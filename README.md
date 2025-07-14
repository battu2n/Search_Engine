# 🔍 Semantic Search Engine

A  semantic search engine built using  **Streamlit**, designed to help users search FAQs or custom documents using natural language queries.

---

## 🧠 Features

- Embeds input documents using `all-MiniLM-L6-v2` model
- Computes semantic similarity with cosine similarity
- Ranks and returns the top-k most relevant results
- Interactive web UI built with **Streamlit**

---

## 🚀 Getting Started

### 🔧 Installation

## 1. Clone the repository:
git clone https://github.com/your-username/semantic-search-engine.git
cd semantic-search-engine

## Install dependencies:

pip install -r requirements.txt

Ensure you have a faq.txt file in the root directory with one document/question per line.

## 3 🖥️ Running the App
Start the Streamlit application:
streamlit run app.py
Then open the provided URL in your browser (usually http://localhost:8501).

## 📁 Project Structure

├── app.py                 # Streamlit frontend
├── search_engine.py       # Core logic for semantic search
├── faq.txt                # Document corpus
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

## 📝 Example Usage:
Type your question in the input field.

Select how many top results to return (1–5).

View the results ranked by semantic similarity score.

## 📚 Sample Documents (faq.txt)

Python is a versatile programming language used for web development, data science, and automation.
Machine learning algorithms can automatically learn patterns from data without explicit programming.
---




