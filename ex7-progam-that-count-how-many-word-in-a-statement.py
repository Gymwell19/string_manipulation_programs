def word_count():
   
    # ask the user for a statement
    statement = input("enter a statement: ")
    
    # split the statement into words
    words = statement.split()
    
    # count the number of words
    word_count = len(words)
    
    # display the number of words
    print("word count: " + str(word_count))

# call the function
word_count()

