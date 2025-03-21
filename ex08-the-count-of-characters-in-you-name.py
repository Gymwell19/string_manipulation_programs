def count_characters():
   
    # ask the user for their full name
    full_name = input("Please enter your name: ")
    
    # count the number of characters
    character_count = len(full_name)
    
    # display the number of characters
    print("the number of characters in your full name is: " + str(character_count))

# call the function
count_characters()