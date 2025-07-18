
# Librerías de apoyo para la visualización de resultados
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

class Doc2VecWrapper(BaseEstimator):
    def _init_(self, max_features=100, epochs=10):
        self.max_features = max_features
        self.epochs = epochs
        self.model = None

    def fit(self, X, y=None):
        tokens = list(map(lambda doc: doc.split(), X))
        self.model = Doc2Vec(sentences = tokens, vector_size = self.max_features, epochs = self.epochs, workers = -1)
        return self

    def transform(self, X):
        Doc2vect_embedding = []
        for i, doc in enumerate(X):
          doc_tokens = doc.split()
          vect = np.zeros(self.max_features)
          for token in doc_tokens:
            if token in self.model.wv.key_to_index:
              vect += self.model.wv[token]

          Doc2vect_embedding.append(vect)
        return np.array(Doc2vect_embedding)


#Pipeline regresión logistica - TF-IDF
pipeline_lr_TFIDF = Pipeline([('vectorizer', TfidfVectorizer()),
                              ('classifier', LogisticRegression(class_weight="balanced"))])


#Pipeline random forest  - TF-IDF
pipeline_rf_TFIDF = Pipeline([('vectorizer', TfidfVectorizer()),
                        ('classifier', RandomForestClassifier(class_weight="balanced", max_samples= 100))])


lr_param_grid = {'vectorizer__max_features': [128,256,512],
                 'classifier__C': [0.01, 0.1, 1, 10]}

rf_param_grid = {'vectorizer__max_features': [128,256,512],
                 'classifier__criterion': ['gini', 'entropy'],
                 'classifier__n_estimators': [10,50,100]}


print('Ejecutando busqueda de hiperparametros de la regresión logistica junto a TF_IDF')
lr_TFIDF_grid_search = GridSearchCV(pipeline_lr_TFIDF, lr_param_grid, cv=5, scoring='f1_macro', verbose=1, n_jobs=-1)
lr_TFIDF_grid_search.fit(X_train, y_train)
print()

print('Ejecutando busqueda de hiperparametros del bsoque aleatorio junto a TF_IDF')
rf_TFIDF_grid_search = GridSearchCV(pipeline_rf_TFIDF, rf_param_grid, cv=5, scoring='f1_macro', verbose=1, n_jobs=-1)
rf_TFIDF_grid_search.fit(X_train, y_train)
print()

