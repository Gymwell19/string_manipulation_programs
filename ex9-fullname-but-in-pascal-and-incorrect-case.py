import random
def convert_to_pascal_case():
   
    # ask the user for their full name
    full_name = input("Please enter your name: ")
    
    # split the full name into words
    words = full_name.split()
    
    # convert each word to Pascal case and join them together
    pascal_case_name = ''.join(letter.capitalize() for letter in words)

    # incorrecting the case of each character
    pascal_case_name = "".join(letter.upper() if random.random() < 0.5 else letter for letter in pascal_case_name)    

    
    # display the full name in Pascal case
    print("your name is: " + pascal_case_name)

# call the function
convert_to_pascal_case()