def city_country(city, country, population=''):
	if population:
		city_name = city + ', ' + country + '- population ' + population
	else:
		city_name = city + ', ' + country
	return city_name.title()



