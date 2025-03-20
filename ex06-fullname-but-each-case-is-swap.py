def incorrect_case():
    # ask the user for their full name
    input_name = input("Please enter your name: ")
    
    # swap the case of each character
    input_name = "".join(letter.lower() if letter.isupper() else letter.upper() for letter in input_name)
    
    # display the string with swapped case
    print("the string with swapped case is: " + input_name)

# call the function
incorrect_case()
