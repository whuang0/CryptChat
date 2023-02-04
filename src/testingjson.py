import json

def write_json(new_data, filename='users.json'):
    with open(filename, 'r+') as file: 

        file_data = json.load(file)
        file_data["user_details"].append(new_data)

        file.seek(0)

        json.dump(file_data, file, indent = 4)

y = {"username":"Other sharan",
    "email": "sharansaha07@gmail.com",
    "password" : "password1234"
    }
z = {
    "username":"Hans",
    "email":"Hans@gmail.com",
    "password":"hanspassword"
}
    
write_json(z)