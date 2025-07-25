
tokens = list(map(lambda doc: doc.split(), X_test))
tagged_corpus = [TaggedDocument(doc, [i]) for i, doc in enumerate(tokens)]
X_test_embeddings = [model_trained.infer_vector(doc.words) for doc in tagged_corpus]
X_test_embeddings = pd.DataFrame(X_test_embeddings)

fig, axes = plt.subplots(1, 2, figsize=(10, 6))

cm = confusion_matrix(y_test, lr_TFIDF_grid_search.predict(X_test))
sns.heatmap(cm, annot=True, cmap='Blues', ax=axes[0])
axes[0].set_title('Regresión logística junto a TF-IDF')

cm = confusion_matrix(y_test, rf_TFIDF_grid_search.predict(X_test))
sns.heatmap(cm, annot=True, cmap='Blues', ax=axes[1])
axes[1].set_title('Bosque aleatorio junto a TF-IDF')


plt.tight_layout()
plt.show()

