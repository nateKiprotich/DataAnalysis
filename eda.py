import read_data as rd
from scipy import stats


df = rd.read_csv()


# Descriptive Statistics
print(df.describe())


# Summarize categorial data
drive_wheels_counts =df["drive-wheels"].value_counts()
#drive_wheels_counts.rename(columns={"drive-wheels":"value_counts"}, inplace=True)
drive_wheels_counts.index.name="drive-wheels"

print(100*"*")

print(drive_wheels_counts)



# Group By
df["price"].replace("?", 0, inplace=True)
df["price"] = df["price"].astype(float)

df_test = df[["drive-wheels","body-style", "price"]]
df_grp = df_test.groupby(["drive-wheels", "body-style"], as_index=False).mean()
print(df_grp)

print(df["price"].dtype)



# Analysis of Variance (ANOVA)
df_annova = df[["make", "price"]]
grouped_annova =df_annova.groupby(["make"])
annova_results_1 = stats.f_oneway(grouped_annova.get_group("honda")["price"], grouped_annova.get_group("subaru")["price"])

print(annova_results_1)
