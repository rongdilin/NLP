# NLP(Natural Language Processing)

## Spam Detector:
dataset: uci machine learning repository.

Sci-kit learn

Naive Bayes

accuracy 87%

binary classifier

## Sentiment Analyzer
dataset: http://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html

NLTK

Lemmatizer

Logstic Regression

sentiment = how positive or negative some text is

## Latent Sentiment Analyzer
multiple words with the same meaning(synonymy)
one word with multiple meanings(polysemy)

PCA(Principal Components Analysis) and SVD(Singular value decomposition)

## Article Spinning
[Take an article and slightly modify it(synonyms, replace phrases that have the same meaning).
Results in a new article with different terms, but same meaning.]

dataset: http://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html

Trigram

## Word Analogy
[find relation among words by Euclidean distance and cosine distance]

dataset: the brown corpus & wikipedia data

word2vec

CBOW = use context to predict middle word

Skip-gram = use middle word to predict context

two version: Numpy & Theano

## Recommender System
[Pretend you are Amazon - match users to products & Netflix - match users to movies.]

frame it as a typical prediction ML problem:

rating = neural_work.predict(X = [user_attributes + product_attributes])

Matrix Factorization

GLoVe: term-term matrix

Numpy Gradient Descent, Theano Gradient Descent, Alternating Least Squares

## Parts-of-Speech Tagging
POS tag is a category you can assign a word, according toits syntactic function.

dataset: http://www.cnts.ua.ac.be/conll2000/chunking/

Logistic regression

Decision Tree 

Baseline F1 score: 0.895, 0.862

RNN F1 score: 0.803, 0.782

HMM F1 score: 0.923, 0.862
