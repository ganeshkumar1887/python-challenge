import pandas as pd
print("Running Status ::")
data = {
    "meter":[25,34,56],
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 