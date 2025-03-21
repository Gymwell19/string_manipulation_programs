def incorrect_case():
    # ask the user for their full name
    input_name = input("Please enter your name: ")
    
    # swap the case of each character
    input_name_swap_case = "".join(letter.lower() if letter.isupper() else letter.upper() for letter in input_name_swap_case)
    
    # display the string with swapped case
    print("your name is: " + input_name_swap_case)

# call the function
incorrect_case()