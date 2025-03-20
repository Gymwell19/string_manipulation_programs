import random
def convert_to_snake_case():
   
    # ask the user for their full name
    full_name = input("Please enter your name: ")
    
    # check if the input is not empty
    if full_name:
       
        # split the full name into words
        words = full_name.split()
        
        # convert each word to lowercase and join them with underscores
        snake_case_name = '_'.join(letter.lower() for letter in words)
        
         # incorrecting the case of each character
        snake_case_name = "".join(letter.upper() if random.random() < 0.5 else letter for letter in snake_case_name)

        # display the full name in snake case
        print("your full name in snake case is: " + snake_case_name)
    else:
        print("Please enter your name.")

# call the function
convert_to_snake_case()
