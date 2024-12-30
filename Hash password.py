import hashlib
import os

# Function to generate a random salt
def generate_salt():
    return os.urandom(8).hex()                       #salt produced will be 16 characters long

# Function to hash a string using SHA-256 with a salt
def generate_hash(password, salt):
    return hashlib.sha256((str(salt) + str(password)).encode()).hexdigest()

# Store user's data
user_data = {}

# Sign-up function
def sign_up():
    username = input("Enter username: ")
    if username in user_data:
        return print("Username already exists. Try a different username.")
        
    
    password = input("Enter password: ")
    salt = generate_salt()
    hashed_password = generate_hash(password, salt)
    user_data[username] = {"salt": salt, "hash": hashed_password}
    print(f"Salt:{salt}")
    print("\n")
    print("Sign-up successful!")

# Login function
def login():
    username = input("Enter username: ")
    if username not in user_data:
      return print("Username not found. Please sign up first.")
      
    password = input("Enter password: ")
    salt = user_data[username]["salt"]
    hashed_password = generate_hash(password, salt)
    if hashed_password == user_data[username]["hash"]:
        print("Login successful!")
    else:
        print("Invalid password. Try again.")

def main():
    while True:
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
                
        if choice == '1':
            print("SIGN UP")
            sign_up()
        elif choice == '2':
            print("LOG IN")
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

main()
