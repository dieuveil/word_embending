from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import numpy as np


# define training data
sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
['this', 'is', 'the', 'second', 'sentence'],
['yet', 'another', 'sentence'],
['one', 'more', 'sentence'],
['and', 'the', 'final', 'sentence']]
# train model
model = Word2Vec(sentences, min_count=1)
# summarize the loaded model
print(model)
# summarize vocabulary
words = list(model.wv.index_to_key)
print(words)
# summarize vectors
print(model.wv.get_normed_vectors())
# save model
#model.save('model.bin')
# load model
#new_model = Word2Vec.load('model.bin')
#print(new_model)


X = model.wv.get_normed_vectors()
pca = PCA(n_components=2)
result = pca.fit_transform(np.array(X))
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
#words = list(model.wv.vocab)
for i, word in enumerate(words):
   pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()