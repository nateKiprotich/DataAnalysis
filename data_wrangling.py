import read_data as rd
import numpy as np
import pandas as pd

df = rd.read_csv()

# Missing Values
# Drop missing values

"""
    inplace=True allows modification to be done on the dataframe

"""
df.dropna(subset=["price"], axis=0, inplace=True) 


# Replace missing values

# Convert column to numeric data typees before performing mean

df["normalized-losses"].replace("?", 0, inplace=True)
df["normalized-losses"] = df["normalized-losses"].astype(float)
mean = df["normalized-losses"].mean()
df["normalized-losses"].replace(0, mean)


#Data Formating
# Convert Liters per Gallon to Litres per KM
# Calculation on the entire column

df["city-mpg"] = 235/df["city-mpg"]

df.rename(columns={"city-mpg": "city-L/100km"}, inplace=True)

# Data Normalization

# Simple Feature scaling 

def simple_feature_scaling(df):

    print(df)
    df = df / df.max()
    print(df)

simple_feature_scaling(df["length"])

# Min-max

def min_max(df):
    print(df)
    df = (df - df.min()) / (df.max() - df.min())
    print(df)

min_max(df["length"])




def z_score(df):
    print(df)
    df = (df-df.mean()) / df.std()
    print(df)

z_score(df["length"])

df["price"].replace("?", 0, inplace=True)
df["price"] = df["price"].astype(float)


# Binning
bins = np.linspace(min(df["price"]), max(df["price"]),4)
group_names = ["Low", "Medium", "High"]
df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)

print(df["price-binned"])

