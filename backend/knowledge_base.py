import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Avoid package-relative imports so the module works when executed
# directly via `flask run` from the backend folder.
import utils


class KnowledgeBase:
    def __init__(self, directory='knowledge_files'):
        self.directory = directory
        self.documents = []
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self.sync()

    def sync(self):
        print("Syncing knowledge base...")
        self.documents = []
        chunks = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if filename.endswith(('.txt', '.md')):
                chunks.extend(utils.parse_txt_md(file_path))
            elif filename.endswith('.docx'):
                chunks.extend(utils.parse_docx(file_path))
            elif filename.endswith(('.xlsx', '.xls')):
                chunks.extend(utils.parse_excel(file_path))
        self.documents = chunks
        if self.documents:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
            print(f"Knowledge base synced. {len(self.documents)} items indexed.")
        else:
            print("Knowledge base is empty or no supported files found.")

    def search(self, query, top_k=3):
        if not self.documents or self.tfidf_matrix is None:
            return []
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        related_docs_indices = cosine_similarities.argsort()[-top_k:][::-1]
        results = []
        for i in related_docs_indices:
            if cosine_similarities[i] > 0:
                results.append(self.documents[i])
        return results