import read_data as rd


df = rd.read_csv()


# Descriptive Statistics
print(df.describe())


# Summarize categorial data
drive_wheels_counts =df["drive-wheels"].value_counts()
#drive_wheels_counts.rename(columns={"drive-wheels":"value_counts"}, inplace=True)
drive_wheels_counts.index.name="drive-wheels"

print(100*"*")

print(drive_wheels_counts)
