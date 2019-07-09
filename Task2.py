# Rajath Akshay Vanikul (29498724)

# Prompt the user to input any number of Morse code sequences until the user decides to stop.
# Display the Morse code for user's reference.
# To exit the input prompt, user must just click on <Enter> without an entry.


# Importing the result of Task1.py to display the Morse code dictionary.
import Task1

# Display the guidelines for user's input.
print("The Morse Code sequences can be of any length but with the minimum of 1 character. \n"
      "Please use displayed Morse code translation table for your reference.\n"
      "Click on <ENTER> twice to terminate and submit your input.")

# Create an empty list to store all the input sequences entered by the user.
input_list = []

# Creating a set of default characters to compare for valid translation.
default_str = set("01*")

# Define an infinite loop to prompt user's input.
# Check the input sequences to just contain '0's,'1's and '*'s and Store all to the list for further operations.
# break the loop if input is "".
while True:
    input_str = input("Enter your Morse Code sequence: ")

    if (input_str == ''):
        break
    if (set(input_str).issubset(default_str)):
        input_list.append(input_str)
        print("sequence: ", input_str)
        print("total input sequence : ", input_list)
    else:
        print("INVALID INPUT, Please enter again.")

# Print the complete input sequence from the user with "*" between input sequences.
morsein_str = "*".join(input_list)
print("total input sequence : ",morsein_str)


