# -*- coding: utf-8 -*-
"""Titanic survival task 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AYlh15F2ev9mesDRzlky61ABm2gcQsX6
"""

import pandas as pd
df = pd.read_csv("/content/tested.csv")
df.head()

df.info

df.corr()

import seaborn as sns
sns.heatmap(df.corr())

df.hist()

df["Age"].hist();

df["Survived"].hist();

import matplotlib.pyplot as plt

sns.countplot(df, x="Survived", hue="Sex")
plt.xlabel('Survived')
plt.ylabel('Count')