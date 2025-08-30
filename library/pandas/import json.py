import pandas as pd 
df = pd.read_json("C:\Users\91778\OneDrive\Desktop\python\library\pandas\flights-1m-parquet.json")
pd.DataFrame(df)
print(df)