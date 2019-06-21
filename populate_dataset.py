# Copyright (c) 2019 Marco Marinello
# See LICENSE file


from centrostudigised import query
import pandas as pd
import progressbar


df = pd.read_csv("dataset.csv")

pg = progressbar.ProgressBar(max_value=len(df))

new_db = {
    "age": [], "sex": [], "cholesterol": [],
    "max_press": [], "smokes": [], "score": []
}
counter = 0

for k in df.iterrows():
    row = dict(k[1])
    del row["Unnamed: 0"]
    for i in row:
        new_db[i].append(row[i])
    new_db["score"].append(query(**row))
    pg.update(counter)
    counter += 1


df = pd.DataFrame(new_db)
print(df.head())
df.to_csv("train.csv")
