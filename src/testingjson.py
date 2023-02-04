import json

def write_json(new_data, filename='users.json'):
    with open(filename, 'r+') as file: 

        file_data = json.load(file)
        file_data["user_details"].append(new_data)

        file.seek(0)

        json.dump(file_data, file, indent = 4)

def has_a_duplicate(new_data, filename='users.json'):
    with open(filename, 'r') as file: 
        users = json.load(file)

        #print(new_data["email"])

        for user in users["user_details"]:
            if (new_data["username"] in user["username"]) or (new_data["email"] in user["email"]) :
                return True
            else: 
                return False

        

y = {"username":"Other sharan",
    "email": "sharansaha07@gmail.com",
    "password" : "password1234"
    }
z = {
    "username":"Hans72",
    "email":"Hans42@gmail.com",
    "password":"hanspassword"
}
    
if (not has_a_duplicate(z)):
    write_json(z)

