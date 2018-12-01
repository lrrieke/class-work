pets = ['abby', 'sparky', 'barnaby']
print ("Is abby in pets? I predict true.")
print ('abby' in pets)
print ("Is alastair in pets? I predict false.")
print ('alastair' in pets)

pet = 'Abby'
print ("Is pet == 'Abby'? I predict true.")
print (pet == 'Abby')
print ("Is pet == 'abby'? I predict false.")
print (pet == 'abby')
print (pet.lower() == 'abby')

lena = 28
print (lena == 28)
patrick = 27
if patrick != 30:
	print ("You are not old enough. Please try again later.")
print (lena < 30)
print (lena > 27)
print (lena <= 28)
print (lena >= 28)
print (lena >= 28 and patrick >= 28)
print (lena <= 28 or patrick <= 28)