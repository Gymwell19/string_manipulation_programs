def print_full_name_in_uppecase():
   
    # ask the user for their full name
    name = input("Please enter your full name: ")
    
    # check if the input is not empty
    if name:
        # convert the full name to all capital letters
        capitalized_name = name.upper()
        
        # display the full name in all capital letters
        print("your full name in all capital letters is: " + capitalized_name)
    else:
        print("Please enter a name.")

# call the function
print_full_name_in_uppecase()