def remove_leading_spaces():
   
    # get the user's full name
    name = input("Please enter your full name: ")
    
    # check if the input is not empty
    
    if name:
        # try to remove any spaces
        cleaned_name = name.lstrip()
        
        # show the name without space
        print("your full name is: " + cleaned_name)
    else:
        print("Please enter a name.")

# call the function
remove_leading_spaces()