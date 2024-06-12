from app import authenticate

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    authenticate(username, password)
