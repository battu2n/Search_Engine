import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SemanticSearchEngine:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.document_embeddings = None
    
    def add_documents(self, documents):
        """Add documents to the search index"""
        self.documents.extend(documents)
        new_embeddings = self.model.encode(documents)
        
        if self.document_embeddings is None:
            self.document_embeddings = new_embeddings
        else:
            self.document_embeddings = np.vstack([self.document_embeddings, new_embeddings])
    
    def search(self, query, top_k=3):
        """Search for most similar documents to the query"""
        if not self.documents:
            return []
        
        # Encode the query
        query_embedding = self.model.encode([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_embedding, self.document_embeddings)[0]
        
        # Get top-k most similar documents
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            results.append({
                'document': self.documents[idx],
                'similarity': similarities[idx],
                'index': idx
            })
        
        return results

# Example usage
# search_engine = SemanticSearchEngine()
# Add some documents
def load_documents(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]
# documents = load_documents('faq.txt')
# search_engine.add_documents(documents)
# # Perform searches
# query = input("Enter your search query: ")

# results = search_engine.search(query, top_k=2)
    
# for i, result in enumerate(results, 1):
#     print(f"{i}. (Score: {result['similarity']:.3f}) {result['document']}")