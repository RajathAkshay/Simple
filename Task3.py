# Rajath Akshay Vanikul (29498724)

# Each Morse code sequence will be processed to translate the sequence into corresponding English alphabets and numbers.
# Display corresponding translated elements in the same sequence.
# Display the invalid sequences entered by the user.


# Display the result from Task1.py for user's reference and import the dictionary.
from Task1 import morse_dict

# Importing the input sequence list from Task2.py for reference.
from Task2 import input_list

# Store the list as a string with "*" between the sequences.
morsein_str = "*".join(input_list)

# Complete input string will be split using "*" as a separator and stored as a list.
morsein_list = morsein_str.split("*")

# Create an empty list to store result.
morseout_list= []

# For all the non-empty elements in the list check if item in list to each key in dictionary,
# Store the corresponding value in sequence.
# Display invalid input if not found in the dictionary.

for item in morsein_list:
    if item != "":
        if item in morse_dict:
            morseout_list.append(morse_dict[item])
        else:
            print(item,"- incorrect item")

# Display the translated output list as a string in sequence.
morseoutput_str= "".join(morseout_list)
print("Translated sequence is : ",morseoutput_str)