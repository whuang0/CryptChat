import json

def cipher(string):
	new1 = ""
	length = len(string)
	for i in range(length):
		ch1 = string[i]
		if (ch1.isspace()):
			new1 += " "
		if(ch1.isupper() and not ch1.isspace()):
			new1 += chr((ord(ch1) + length - 65) % 26 + 65)
		if(ch1.islower() and not ch1.isspace()):
			new1 += chr((ord(ch1) + length - 97) % 26 + 97)
	return new1

def decipher(string):
	new1 = ''
	length = len(string)
	for i in range(length):
		ch1 = string[i]
		if (ch1.isspace()):
			new1 += " "
		if(ch1.isupper() and not ch1.isspace()):
			new1 += chr((ord(ch1) - length - 65) % 26 + 65)
		if(ch1.islower() and not ch1.isspace()):
			new1 += chr((ord(ch1) - length - 97) % 26 + 97)
	return new1

def get_credentials(index):
	with open("users.json", "r") as file:
		users = json.load(file)
		username = users["user_details"][index]["username"]
		email = users["user_details"][index]["email"]
		password = users["user_details"][index]["password"]
		return [username, email, password]

def override_to_encrypted(index):
	encrypted_username = cipher(get_credentials(index)[0])
	encrypted_email = cipher(get_credentials(index)[1])
	encrypted_password = cipher(get_credentials(index)[2])
	with open("users.json", 'r+') as file:
		users = json.load(file)
		file.seek(0)
		users["user_details"][index].update({"username":(encrypted_username),"email" : (encrypted_email), "password" : (encrypted_password)})
		json.dump(users, file, indent = 4)
		file.truncate()

def retrieve_username(email):
	cipheredEmail = cipher(email)
	with open('users.json') as data_file:    
		data = json.load(data_file)
		print(data["user_details"][0])
	for index in data["user_details"]:
		print(data["user_details"][index][2])
		# if(data["user_details"][index]["email"] != cipheredEmail):
		# 	index = index + 1
		# else:
		# 	decrypted_username = decipher(get_credentials(index)[0])
		# 	return decrypted_username

def retrieve_password(index):
	decrypted_password = decipher(get_credentials(index)[2])
	return decrypted_password

def main():
	# override_to_encrypted(0)
	# override_to_encrypted(1)
	retrieve_username("s12@gmail.com")
main()
	
		
				
			

