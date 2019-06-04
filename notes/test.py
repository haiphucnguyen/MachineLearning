#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


import warnings;
warnings.simplefilter('ignore')

colNames = ['Age', 'WorkClass', 'FnlWgt', 'Education', 'Education-Num', 'Marital-Status', 'Occupation',
            'Relationship', 'Race', 'Sex', 'Capital-Gain', 'Capital-Loss', 'Hours-Per-Week', 'Native-Country', 'Salary']
dataset_train = pd.read_csv('data/adult-train.csv', header=None, names = colNames)
dataset_train.head(10)

dataset_test = pd.read_csv('data/adult-test.csv', header=None, names = colNames)
dataset_test.head(10)

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler

# Check code https://www.kaggle.com/jeffd23/scikit-learn-ml-from-start-to-finish#Some-Final-Encoding to encode the
# category values to numerical values


labelEncoder = LabelEncoder()
dataset_train = dataset_train.apply(labelEncoder.fit_transform)
dataset_test = dataset_test.apply(labelEncoder.fit_transform)

dropColumns = ['Salary', 'Education']
X_train = dataset_train.drop(dropColumns, axis=1)
Y_train = dataset_train['Salary']

X_test = dataset_test.drop(dropColumns, axis=1)
Y_test = dataset_test['Salary']

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from autosklearn.classification import AutoSklearnClassifier

cls = AutoSklearnClassifier()
cls.fit(X_train, Y_train)

predictions = cls.predict(X_test)