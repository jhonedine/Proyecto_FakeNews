
"""TF - IDF"""

corr_matrixTFIDF = TFIDFembedding.corr()
corr_matrix_dv = doc2vect_embedding.corr()


fig, axes = plt.subplots(1, 2, figsize=(20, 5))


sns.heatmap(corr_matrixTFIDF, annot=False, cmap='coolwarm', ax=axes[0])
axes[0].set_title('Mapa de correlaciones TF-IDF')

sns.heatmap(corr_matrix_dv, annot=False, cmap='coolwarm', ax=axes[1])
axes[1].set_title('Mapa de correlaciones Doc-to-vect')

plt.tight_layout()
plt.show()

doc2vect_embedding['puntuacion'] = y_tune.tolist()

corr_matrix_dv = doc2vect_embedding.corr()


dv_obj_corr = corr_matrix_dv['puntuacion']
dv_obj_corr = dv_obj_corr[dv_obj_corr!=1]



obj_corr = pd.DataFrame()

obj_corr['value'] =  dv_obj_corr.tolist()

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

sns.histplot(data=obj_corr, x='value', kde=True)
axes.set_title('Histograma de correlaciones de la representación a la variable objetivo')

plt.tight_layout()
plt.show()


