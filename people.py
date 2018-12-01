people = {
	'renee' : {
		'first name' : 'renee',
		'last name' : 'rieke',
		'location' : 'las vegas',
		'age' : '55'
		},

	'patrick' : {
		'first name' : 'patrick',
		'last name' : 'caddick', 
		'location' : 'las vegas', 
		'age' : '27'
		},

	'lena' : {
		'first name' : 'lena',
		'last name' : 'rieke',
		'location' : 'las vegas',
		'age' : '28'
		},
	}

for person, person_info in people.items():
	print("\nFull name: " + person_info['first name'].title() + " " + person_info['last name'].title())
	print("\nLocation: " + person_info['location'].title())
	print("\nAge: " + person_info['age'].title())