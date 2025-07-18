
doc2vect_embedding.shape

tokens = list(map(lambda doc: doc.split(), X_test))
tagged_corpus = [TaggedDocument(doc, [i]) for i, doc in enumerate(tokens)]
X_test_embeddings = [model_trained.infer_vector(doc.words) for doc in tagged_corpus]
X_test_embeddings = pd.DataFrame(X_test_embeddings)


X_test_embeddings

import xgboost as xgb
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.preprocessing import LabelEncoder

tokens = list(map(lambda doc: doc.split(), X_train))
tagged_corpus = [TaggedDocument(doc, [i]) for i, doc in enumerate(tokens)]
X_train_embeddings = [model_trained.infer_vector(doc.words) for doc in tagged_corpus]
X_train_embeddings = pd.DataFrame(X_train_embeddings)


if not pd.api.types.is_numeric_dtype(y_train):
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)

model = xgb.XGBClassifier(
    objective='binary:logistic',
    eval_metric='logloss',
    random_state=42,
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1
)

model.fit(X_train_embeddings, y_train)


y_pred = model.predict(X_test_embeddings)
print(classification_report(y_test, y_pred))
print("F1-Score:", f1_score(y_test, y_pred))


from sklearn.metrics import confusion_matrix




