import read_data as rd

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

