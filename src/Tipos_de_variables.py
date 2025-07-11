
import textstat
import numpy as np
import matplotlib.pyplot as plt

nlp = spacy.load('en_core_web_sm')

# Calidad del vocabulario (palabras reconocidas en el vocabulario de spaCy)
token_quality = df['text'][:1000].map(lambda x: np.mean([token.lemma_ in nlp.vocab for token in nlp(str(x))]))

# Legibilidad con Flesch Reading Ease (inglés)
reading_quality = df['text'][:1000].map(lambda x: textstat.flesch_reading_ease(str(x)))

# Gráficas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Legibilidad y calidad del texto de las noticias')

# Histograma de palabras reconocidas
ax1.hist(token_quality, bins=50, color='skyblue', edgecolor='black')
ax1.set_title('Palabras reconocidas por spaCy')
ax1.set_xlabel('% de palabras reconocidas')
ax1.set_ylabel('Frecuencia')

# Histograma de legibilidad
ax2.hist(reading_quality, bins=50, color='salmon', edgecolor='black')
ax2.set_title('Índice Flesch Reading Ease (Inglés)')
ax2.set_xlabel('Puntaje de legibilidad')
ax2.set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()

"""De esto podemos concluir que el corpus que estamos analizando tiene una facilidad de lectura moderada."""


"""Relación Entre Variables""

cross_tab = pd.crosstab(df['subject'], df['type'], normalize='index')
sns.heatmap(cross_tab, annot=True, cmap="YlGnBu")
plt.title('Relación entre Subject y Tipo de Noticia (Real o Falsa)')
plt.show()

"""Relacion Fake y Real News"""

sns.countplot(x='type', data=df, color='r')
plt.title("Distribution of Fake vs Real News")
plt.xlabel("News Type")
plt.ylabel("Number of Articles")
plt.xticks([0, 1], ['Fake', 'Real'])
plt.show()


