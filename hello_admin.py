current_users = ['lena', 'patrick', 'renee', 'raymond', 'elizabeth']

new_users = ['john', 'lena', 'david', 'lydia', 'raymond']

for new_user in new_users:
	if new_user in current_users:
		print("Sorry, " + new_user + " is already in use. Please pick another username.")
	else:
		print("Congratulations, " + new_user + " is available!")