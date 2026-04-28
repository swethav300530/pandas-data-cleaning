import pandas as pd
import numpy as np

data = {
    "Name": ["A", "B", "C", None],
    "Age": [23, np.nan, 25, 22]
}

df = pd.DataFrame(data)

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Drop rows with missing Name
df = df.dropna(subset=["Name"])

print(df)

df = pd.DataFrame({
    "Name": ["A", "B", "A", "C"],
    "Age": [23, 25, 23, 30]
})

df = df.drop_duplicates()
print(df)

df = pd.DataFrame({
    "name": ["A", "B"],
    "age": [20, 25]
})

df = df.rename(columns={"name": "Name", "age": "Age"})
print(df)

df["Age"] = df["Age"].astype(int)

df["Age"] = df["Age"].astype(int)

df = pd.DataFrame({"Salary": [10000, 20000, 300000, 25000]})

# Remove extreme values
df = df[df["Salary"] < 100000]
print(df)

df = pd.DataFrame({"Name": ["  swetha ", "ANU ", " Ravi"]})

df["Name"] = df["Name"].str.strip().str.lower()
print(df)

df = pd.DataFrame({"Gender": ["M", "F", "Male", "Female"]})

df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "F": "Female"
})

print(df)