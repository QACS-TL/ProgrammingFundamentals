mylist = [30, 5, 100, 90, 7]
# mylist.append(45)
# mylist.append(70)
# mylist.remove(90)

#mylist[2] += 100

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[len(mylist) - 1])
sorted_list = sorted(mylist)
print(sorted_list)
# mylist.sort()
print(mylist)

print("**** Tuple Fun ****")
mytuple = (30, 56, 35, 90, 78)
print(mytuple)
print(mytuple[3])
# mytuple[2] += 100
# mytuple.append(3)

print("**** Set fun ****")
myset = {12, 45, 67, 45}
myotherset = {23, 67, 22}
myset.add(78)

print(myset.intersection(myotherset))

print("**** dictionary fun ****")
mydictionary = {
    "DB001": ["Ted Smith", "0123454545", "1 the High street"],
    "M234": ["Tina Jones", "0234121212", "34 the highway"],
    "D002": ["Kamran Sadiq", "03123676767", "4 Bishops Avenue"]
}

print(mydictionary["M234"][1])


print("**** Looping fun ****")

for i in range(0, 5):
     mylist[i] = mylist[i] * mylist[i]
print(mylist)

for item in mylist:
    item = item * item

j = 0
while j < len(mylist):
    mylist[j] = mylist[j] * mylist[j]
    j += 1

j = 0
while True:
    mylist[j] = mylist[j] * mylist[j]
    if j == len(mylist) - 1:
        break
    else:
        j += 1


print(mylist)

salaries = [1500, 35000, 50000, 200000]

for salary in salaries:
    print(f"Salary: {salary}")
    highTax = 0
    lowTax = 0
    superTax = 0

    if salary >= 11850 and salary <= 46350:
        lowTax += (salary - 11850) * 0.2
    elif salary >= 46351 and salary <= 150000:
        lowTax += (46350 - 11850) *0.2
        highTax+=(salary-43000)*0.4
    elif salary > 150000:
        lowTax += (46350 - 11850) * 0.2
        highTax += (150000 - 46350) * 0.4
        superTax += (salary - 150000) * 0.45
    else:
        print("Tax Free!")

    print(f"Low tax: £{lowTax}")
    print(f"High tax: £{highTax}")
    print(f"Super tax: £{superTax}")
    print("")



masterPIN = "1234"
pin = ""

retries = 0
while pin != masterPIN and retries < 3:
    pin = input("Enter PIN:")
    if pin == masterPIN:
        print("Access Granted")
        break
    else:
        print("Invalid PIN")
        retries += 1

if retries == 3:
    exit(0)
print("We will only see this if valid pin entered!")