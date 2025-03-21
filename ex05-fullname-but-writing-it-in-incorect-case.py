import random

def incorrect_case():
   
    # ask the user for a full name
    input_name = input("Please enter your name: ")
    
    # incorrecting the case of each character
    input_name_incorrect_case = "".join(letter.upper() if random.random() < 0.5 else letter for letter in input_name_incorrect_case)    
   
    # display the full name with swapped case
    print("you name is: " + input_name_incorrect_case)

# call the function
incorrect_case()