import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split as tts
import pickle

dataIris = load_iris()
df = pd.DataFrame(dataIris["data"], columns= ["SL", "SW", "PL", "PW"])
df["target"] = dataIris["target"]
df["species"] = df["target"].apply(lambda x : dataIris["target_names"][x])

xtr, xts, ytr, yts = tts(df[["SL", "SW", "PL", "PW"]], df["species"], test_size= .1)

model = LogisticRegression(solver= "lbfgs", multi_class= "auto", max_iter= 100000)
model.fit(xtr, ytr)

with open("modelPickle", "wb") as modPkl:
    pickle.dump(model, modPkl)