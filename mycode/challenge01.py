#!/usr/bin/python3

fruitcompanies= [{"name":"Zesty","employees":["Ambu","Brent", "Bryan","Carlee","Chad"]},
                 {"name":"Ripe.ly","employees":["Darlene","Eric","Fernando","Peter",]},
                 {"name":"FruitBee","employees":["Jennae","Joel","Jonas","Josh",]},
                 {"name":"JuiceGrove","employees":["Kurt","Nate","Patrick","Rachel",]}]

# challenge function 01
print("Challenge function 01")
for i in fruitcompanies[0]["employees"]:
	print(i)


#challenge function 02
print("")
print("Challenge function 02")
companies = []
for i in fruitcompanies:
	companies.append(i["name"])

name = input(f"pick a name from {companies} : ")
for i in fruitcompanies:
	if i["name"].lower() == name.lower():
		for x in i["employees"]:
			print(x)

#Challenge function 03
print("")
print("Challenge function 03")
companies = []
for i in fruitcompanies:
	companies.append(i["name"])

name = input(f"pick a name from {companies} : ")
for i in fruitcompanies:
	if i["name"].lower() == name.lower():
		for x in i["employees"]:
			if x != "Chad":
				print(x)
