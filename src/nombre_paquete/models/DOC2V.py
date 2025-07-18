
model = Doc2Vec(
        documents = tagged_corpus,
        vector_size = 100,
        epochs = 20,
        workers = -1
        )

vect = model.infer_vector(tagged_corpus[0].words)
display(vect)
display(vect.shape)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['type'], test_size=0.15, random_state=42)
X_train, X_tune, y_train, y_tune = train_test_split(X_train, y_train, test_size=0.1765, random_state=42)

print(f'Numero de registros en train: {len(X_train)}')
print(f'Numero de registros en tune: {len(X_tune)}')
print(f'Numero de registros en test: {len(X_test)}')

tokens = list(map(lambda doc: doc.split(), X_train))
tagged_corpus = [TaggedDocument(doc, [i]) for i, doc in enumerate(tokens) ]

model_trained = Doc2Vec(
                        documents = tagged_corpus,
                        vector_size = 500,
                        epochs = 20,
                        workers = -1 )

tokens = list(map(lambda doc: doc.split(), X_tune))
tagged_corpus = [TaggedDocument(doc, [i]) for i, doc in enumerate(tokens)]
doc2vect_embedding = []

for i, doc in enumerate(tagged_corpus):
  vect = model_trained.infer_vector(doc.words)
  doc2vect_embedding.append(vect)
  #print(f'{i} of {len(tagged_corpus)}', end='')

doc2vect_embedding = pd.DataFrame(doc2vect_embedding)
doc2vect_embedding.head()

