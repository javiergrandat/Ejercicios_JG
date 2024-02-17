import pandas as pd

dict = {
"country":["Brazil","Russia","India","China","South Africa"],
"capital":["Brasilia","Moscow","New Delhi","Beijing","Pretoria"],
"area":[8.516, 17.10, 3.286, 9.597, 1.221],
"population":[200.4, 143.5, 1252, 1357, 52.98] 
}

dogs = pd.read_csv("dogs.csv", index_col=0)
#brics = pd.DataFrame(dict)
dogs.reset_index(inplace = True)

print(dogs.head())
print(dogs.info())
print(dogs.shape)
print(dogs.describe())
print(dogs.values)
print(dogs.columns)
print(dogs.index)
print(dogs.sort_values("Weight (kg)", ascending=False))
print(dogs[dogs["Date of Birth"] < "2015-01-01"])
print(dogs["Height (cm)"].mean())
dogs.set_index("Name",inplace = True)
print(dogs)
