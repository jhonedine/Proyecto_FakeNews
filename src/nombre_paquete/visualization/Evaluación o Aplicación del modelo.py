

#MATRIX DE CONFUSIÓN
fig, axes = plt.subplots(1, 2, figsize=(10, 6))

cm = confusion_matrix(y_test, lr_TFIDF_grid_search.predict(X_test))
sns.heatmap(cm, annot=True, cmap='Blues', ax=axes[0])
axes[0].set_title('Regresión logística junto a TF-IDF')

cm = confusion_matrix(y_test, rf_TFIDF_grid_search.predict(X_test))
sns.heatmap(cm, annot=True, cmap='Blues', ax=axes[1])
axes[1].set_title('Bosque aleatorio junto a TF-IDF')


plt.tight_layout()
plt.show()


print(classification_report(y_test, lr_TFIDF_grid_search.predict(X_test)))

