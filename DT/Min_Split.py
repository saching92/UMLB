import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



########################## DECISION TREE #################################


### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively

from sklearn import tree
from sklearn.metrics import accuracy_score

#### your code goes here


clf = tree.DecisionTreeClassifier(min_samples_split=2)
clf.fit(features_train, labels_train)   
pred = clf.predict(features_test)

acc_min_samples_split_2 = accuracy_score(pred, labels_test)
### be sure to compute the accuracy on the test set
print acc_min_samples_split_2

clf = tree.DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train, labels_train)   
pred = clf.predict(features_test)

acc_min_samples_split_50 = accuracy_score(pred, labels_test)
### be sure to compute the accuracy on the test set
print acc_min_samples_split_50




def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}
