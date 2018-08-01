candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]
allowance = 5
candyCart = []
for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)
for x in range(allowance):
    selected = input("Which candy do you want?")

