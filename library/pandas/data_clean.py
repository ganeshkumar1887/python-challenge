import pandas as pd

df = pd.read_csv(r"C:\Users\91778\OneDrive\Desktop\python\library\pandas\csvfile.csv")

new_df = df.dropna()

print(new_df.to_string())