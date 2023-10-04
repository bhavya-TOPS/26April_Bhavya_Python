# Write a Python script to merge two Python dictionaries 

data1 = {"a":100, "b":100, "c":100}

data2 = {"a":200, "b":200, "c":200}

data = data1.copy

data.update(data2)

print(data)
