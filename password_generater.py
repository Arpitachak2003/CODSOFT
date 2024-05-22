import random
import string

def generate_password(length,complexity):
    # Define the character sets for different complexity levels
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets based on user's desired complexity 
    if complexity == 1 :
        all_chars = lower_case + upper_case
    elif complexity == 2 :
        all_chars = lower_case + upper_case + digits
    elif complexity == 3 :
        all_chars = lower_case + upper_case + digits + special_chars

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    # Prompt user for password length
    length = int(input("Enter the desired length of the password : "))
    complexity = int(input("Choose complexity : \n1 - Easy\n2 - Medium\n3 - Hard\nEnter Your Option :  "))
            
    if length <= 0:
        print("Please enter a valid positive integer.")
    elif complexity not in [1,2,3] :
        print("Choose a valid Complexity")
    else :
        # Generate and display the password
        password = generate_password(length,complexity)
        print("Generated Password :", password)

if __name__ == "__main__":
    main()


