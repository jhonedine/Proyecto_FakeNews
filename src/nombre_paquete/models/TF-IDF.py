
from sklearn.feature_extraction.text import TfidfVectorizer

TFIDF_vectorizer = TfidfVectorizer(max_features=512)
TFIDF_vectorizer.fit(X_train)
TFIDFembedding = TFIDF_vectorizer.transform(X_tune)
TFIDFembedding = pd.DataFrame(TFIDFembedding.toarray())
TFIDFembedding.columns = TFIDF_vectorizer.get_feature_names_out()

TFIDFembedding.head()

