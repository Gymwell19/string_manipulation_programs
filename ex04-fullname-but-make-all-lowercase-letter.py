def print_full_name_in_lowercase():
   
    # ask the user for their full name
    full_name = input("Please enter your full name: ")
    
    # check if the input is not empty
    if full_name:
        # convert the full name to all lowercase letters using the lower() method
        full_name_in_lowercase = full_name.lower()
        
        # display the full name in all lowercase letters
        print("your full name in all lowercase letters is: " + full_name_in_lowercase)
    else:
        print("Please enter a name.")

# call the function
print_full_name_in_lowercase()