import pandas as pd
df=pd.read_csv("main.csv")
print(df.shape)
del df["right_ascension"]
print(df.shape)
del df["declination"]
print(df.shape)
del df["host_temperature"]
print(df.shape)
del df["host_radius"]
print(df.shape)
df.to_csv("new.csv")