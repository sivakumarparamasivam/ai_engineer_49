password = "openAI123"
MAX_RETRIES = 3
attempts = 0
while attempts < MAX_RETRIES:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect password. You have {MAX_RETRIES - attempts} attempts left.")
else:
    print("Access denied. Too many incorrect attempts.")