nestedList = [[j for j in range(5)] for i in range(5)]
print(nestedList)

slicesList = [0, 10, 20, 30, 40, 50, 60]
print(slicesList[2:5])

filterList = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 70, filterList)
print(list(filtered))

x = [1, 2, 3, 4, 5]
x.remove('3')