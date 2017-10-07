# Naive Bayes spam detection

# dataset: https://archive.ics.uci.edu/ml/datasets/Spambase

from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np

# Note: technically multinomial NB is for "counts", but the documentation says
#       it will work for other types of "counts", like tf-idf, so it should
#       also work for our "word proportions"

data = pd.read_csv('spambase.data').as_matrix() # use pandas for convenience
np.random.shuffle(data) # shuffle each row in-place, but preserve the row

X = data[:,:48]
Y = data[:,-1]

# last 100 rows will be test
X_train = X[:-100,]
Y_train = Y[:-100,]
X_test = X[-100:,]
Y_test = Y[-100:,]

model = MultinomialNB()
model.fit(X_train, Y_train)
print "Classification rate for NB:", model.score(X_test, Y_test)