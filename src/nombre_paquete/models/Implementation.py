
!pip install gensim
!pip install unidecode gensim scipy
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
tokens = list(map(lambda doc: doc.split(), corpus))
tagged_corpus = [
        TaggedDocument(doc, [i])
        for i, doc in enumerate(tokens)
        ]
        
display(tagged_corpus[-1])
