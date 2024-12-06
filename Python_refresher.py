# Simple program to get user details

# Function to collect user information
def get_user_info():
    # Get user input
    name = input("Please enter your name: ")
    user_id = input("Please enter your ID: ")
    address = input("Please enter your address: ")

    # Display the collected information
    print("\nUser Information:")
    print(f"Name: {name}")
    print(f"ID: {user_id}")
    print(f"Address: {address}")

# Call the function
get_user_info()