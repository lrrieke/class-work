alien_0 = {'color' : 'green', 'points' : 5}

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

user_0 = {
	'username' : 'efermi',
	'first': 'enrico',
	'last' : 'fermi',
}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: "+ value)

favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
} 

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

aliens = []

for alien_number in range(0, 30):
	new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = '10'

for alien in aliens[0:5]:
	print(alien)
print("...")

pizza = {
	'crust' : 'thick',
	'toppings' : ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
	'jen' : ['python', 'ruby'],
	'sarah' : ['c'],
	'edward' : ['ruby', 'go'],
	'phil' : ['python', 'haskell']
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() +"'s favorite languages are: ")
	for language in languages:
		print("\t" + language.title())

users = {
	'aeinstein' : { 
		'first' : 'albert',
		'last' : 'einstein',
		'location' : 'princeton',
		},
	'mcurie' : {
		'first' : 'marie',
		'last' : 'curie',
		'location' : 'paris'
		}, 

	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull name: " +full_name.title())
	print("\tLocation: " + location.title())

