topFive = ["Star Wars", "Jaws", "Postman Pat 2", "Vanilla Sky", "Absolutely Fabulous"]
print(topFive)
print("Second favourite Movie" + topFive[1])
topFive.append("One Flew over the Cuckoos nest")
print(topFive)
print(len(topFive))
# topFive[len(topFive)-1] = "It's a wonderful life"
# OR
topFive[-1] = "It's a Wonderful Life" # python allows offset from end of list by using negative numbers
print(topFive)
topFiveSorted = sorted(topFive)
print(topFiveSorted)
