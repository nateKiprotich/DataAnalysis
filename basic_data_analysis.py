import read_data as rd

df = rd.read_csv()

#show datatype
print(df.dtypes)

# Print the first 5 rows
print(df.head())

#print last first rows
print(df.tail())

#Statistical Summary of numeric columns
print(df.describe())

#Summary of all columns
print(df.describe(include='all'))

#Summary info
print(df.info())
