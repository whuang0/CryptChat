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

def get_credentials(email):
	with open("users.json", "r") as file:
		users = json.load(file)
		username = users.get(cipher(email))
		password = users.get(cipher(email))
		return [username, password]

def insert_credentials(email, username, password):
	encrypted_username = cipher(username)
	encrypted_email = cipher(email)
	encrypted_password = cipher(password)
	with open("users.json", 'r+') as file:
		try:
			users = json.load(file)
		except:
			users = {}
		if(users.get(encrypted_email) != None):
			print('user already exists')
			return
		file.seek(0)
		users[encrypted_email] = {"username":encrypted_username, "password":encrypted_password}
		json.dump(users, file, indent = 4)

def retrieve_record(email):
	cipheredEmail = cipher(email)
	with open('users.json') as data_file:    
		data = json.load(data_file)
		return data.get(cipheredEmail)

def insert_msgs(msg):
	encrypted_msg = cipher(msg)
	with open("group.json", 'r+') as file:
		data = json.load(file)
		file.seek(0)
		json.dump(encrypted_msg, file, indent = 4)


def main():
	insert_credentials("s123@gmail.com", "sharan", "pass")
	insert_credentials("ab23@gmail.com", "andy", "pass2")
	insert_msgs("hello")
main()
	
		
				
			

