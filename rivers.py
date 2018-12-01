rivers = { "nile" : "egypt", "lena" : "russia", "danube" : "austria"}

for name, country in rivers.items():
	print("The " + name.title() + " River runs through " + country.title() + ".")

for name in rivers.keys():
	print(name.title())

for county in rivers.values():
	print(county.title())