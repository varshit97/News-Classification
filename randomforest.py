
from __future__ import division
import numpy as np
from scipy.stats import mode
from utilities import shuffle_in_unison
from decisiontree import DecisionTreeClassifier

class RandomForestClassifier(object):
    def __init__(self, n_estimators=32, max_features=np.sqrt, max_depth=10, min_samples_split=2, bootstrap=0.9):
        self.n_estimators = n_estimators
        self.max_features = max_features
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.bootstrap = bootstrap
        self.forest = []

    def fit(self, X, y):
        self.forest = []
        n_samples = len(y)
        n_sub_samples = round(n_samples*self.bootstrap)
        for i in xrange(self.n_estimators):
            shuffle_in_unison(X, y)
            X_subset = X[:n_sub_samples]
            y_subset = y[:n_sub_samples]
            tree = DecisionTreeClassifier(self.max_features, self.max_depth, self.min_samples_split)
            tree.fit(X_subset, y_subset)
            self.forest.append(tree)

    def predict(self, X):
        n_samples = X.shape[0]
        n_trees = len(self.forest)
        predictions = np.empty([n_trees, n_samples])
        for i in xrange(n_trees):
            predictions[i] = self.forest[i].predict(X)
        return mode(predictions)[0][0]

    def score(self, X, y):
        y_predict = self.predict(X)
        n_samples = len(y)
        correct = 0
        for i in xrange(n_samples):
            if y_predict[i] == y[i]:
                correct = correct + 1
        accuracy = correct/n_samples
        return accuracy
