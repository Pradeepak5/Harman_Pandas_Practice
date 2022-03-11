import pandas as pd
df=pd.read_csv("FuelConsumption.csv")
print(df.head(1))
print(df.tail(1))
print(df.info())