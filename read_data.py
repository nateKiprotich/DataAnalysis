import pandas as pd


path = './Data/'
file_name = 'imports-85.data'

file_path_name = path+file_name

headers = ["symboling", "normalized-losses","make", "fuel-type", "aspiration", "num-of-doors",
        "body-style", "drive-wheels","engine-location", "wheel-base", "length","width", "height",
        "curb-weight", "engine-type", "num-of-cylinders","engine-size", "fuel-system", "bore",
        "stroke","compression-ratio","horsepower", "peak-rpm",  "city-mpg",  "highway-mpg", "price"]

df = pd.read_csv(file_path_name, header=None)

df.columns = headers

print(df.head())


save_data_path = "./Data/Saved Data/"
data_name = "autos.csv"
file_name = save_data_path + data_name

df.to_csv(file_name)
