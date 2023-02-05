import json

def save_to_json(email, username, password):
    user = {
        "email": email,
        "username": username,
        "password": password
    }
    with open("users.json", "a") as file:
        file.write(json.dumps(user))
        file.write("\n")

if __name__ == "__main__":
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")
    save_to_json(email, username, password)
