import pandas as pd
import numpy as np


def analyse_iris():
    with open("iris.csv", "r") as iris:
        df = pd.read_csv(iris)
    df2 = df.to_dict()
    petals = []
    petals.append(np.mean(np.asarray(list(df2["petal.length"].values()))))
    petals.append(np.median(np.asarray(list(df2["petal.length"].values()))))
    petals.append(np.std(np.asarray(list(df2["petal.length"].values()))))
    print("Statystyka dla długości płatków to: średnia = {:0.4}, "
          "mediana = {}, std = {:0.4}".format(petals[0], petals[1], petals[2]))


if __name__ == "__main__":
    # print("Hello World!")
    analyse_iris()