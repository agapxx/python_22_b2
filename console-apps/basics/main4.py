#Python Data Structures
#Lists 'var = []'
genders = ['Male', 'Female', 'Bob Risky', 'James Brown', 'LGBTQ', 'Straight', 'Shemale', 2000, True, False]

gendersee = (("sdd","sddds"))


print(genders)


# list, dictionaries, tuple have these characteristics: # Ordering , Changeability , Redundancy
# list have order, they allow duplicate



#to list each item you use a loop
for gender in genders:
    print(gender)

genders[4] = "LGBQT"
print(genders)

genders[2:4] = ["BRisky","Jbrown"]
print(genders)

genders.insert(2, "Undisclosed")
print(genders)

laptopBrand = ["Dell", "Razer Blade", "Asus", "MSI"]
favyBrands = ['Toshiba', "Zinox", "Sony"]
print(laptopBrand)
laptopBrand.append("HP")
print(laptopBrand)
laptopBrand.extend(favyBrands)
print(laptopBrand)

laptopBrand.remove("HP")
print(laptopBrand)

laptopBrand.pop(5)
print(laptopBrand)
laptopBrand.pop()
print(laptopBrand)

del laptopBrand[1]
print(laptopBrand)

# del laptopBrand
# print(laptopBrand)

l=0
while l < len(laptopBrand):
    print(laptopBrand[l])
    l += 1

print("Using list comprehension")
[print(item) for item in laptopBrand]

laptopBrand.reverse()
print(laptopBrand)

laptopBrand.sort(reverse=True)
print(laptopBrand)

laptopBrand.append("Dell")
laptopBrand.append("Dell")
laptopBrand.append("Dell")
laptopBrand.append("Dell")
print(laptopBrand.count("Dell"))

print(laptopBrand.count("Dell"))
print(laptopBrand)

laptopBrand.clear()
print(laptopBrand)


#Dictionaries  - 'var = {key : value, key : value}'
favyFC = {
    "name": "Chelsea FC",
    "established": 1905,
    "stadium": "Stamford bridge",
    "nick": "blues",
    "nick": "the blues",
    "cups": ['2020 world champions']
}

favyCar = {
    "brand": "Innoson",
    "model": "Ikenga",
    "year": 2021,
    "mileage": 17500,
    "hp": 280
}

print(favyFC["name"])
print(favyFC["established"])

print(len(favyFC))

clubName = favyFC.get("name")
print(f"My dearest football club is {clubNmae}")

theKeys = favyFC.Keys()
print(theKeys)

theVals = favyFC.values()
print(theVals)

theVals = favyFC.values()
print(theVals)

theItems = favyFC.items()
print(theItems)












