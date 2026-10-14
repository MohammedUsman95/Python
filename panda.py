import pandas

data = {
    "Name": ["Rahul", "Aisha", "Karan", "Priya", "Arjun"],
    "Score": [85, 92, 76, 68, 89]
}

dataframe = pandas.DataFrame(data)
dfsorted = dataframe.sort_values("Score")

print(dataframe)
print(dataframe.info())
print("Sum = ", dataframe["Score"].sum())

print(dfsorted)
print("Shape = ", dfsorted.shape)
print(dfsorted.head())
print(dfsorted.describe())
