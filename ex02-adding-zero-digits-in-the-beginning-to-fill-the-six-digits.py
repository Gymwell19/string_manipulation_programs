def add_zero_number():
   
    # Prompt the user to enter a number within a specified range.
    number = int(input("Please enter a number from 0-1000: "))
    if 0 <= number <= 1000:
   
        # Convert the integer to a string and add it with leading zeros
        six_digit_number = str(number).zfill(6)
        
        # Display the formatted number
        print(six_digit_number)
    else:
        print("Please enter a number between 0 and 1000.")

# call the function again
add_zero_number()



