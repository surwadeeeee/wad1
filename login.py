# Sample user credentials (replace with your own database or authentication mechanism)
user_database = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def login():
    # Get user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered username exists in the user_database and if the password is correct
    if username in user_database and user_database[username] == password:
        print("Login successful. Welcome, {}!".format(username))
    else:
        print("Invalid username or password. Please try again.")

# Example usage
login()
