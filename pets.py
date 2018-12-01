pets = {
	'abigail' : {
		'species' : 'dog',
		'owner' : 'lena'
		},
	'janie' : {
		'species' : 'cat',
		'owner' : 'patrick'
		},
	'barnaby' : {
		'species' : 'rabbit',
		'owner' : 'lena'
		}	
	}

for pet, pet_info in pets.items():
	print("\nPet: " + pet.title())
	print("\nKind of animal: " + pet_info['species'].title())
	print("\nOwner: " + pet_info['owner'].title())