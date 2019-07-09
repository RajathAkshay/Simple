# Rajath Akshay Vanikul (29498724)

# The decoded output sequence is analysed to find occurrence of each character.

# Impoting translated final output sequence from Task3.py for analysis
from Task3 import morseoutput_str

# Creating an empty dictionary to store occurrences of each character in output sequence.
occurrence_dict = {}

# Check for every character in output sequence to occurrence dictionary.
# Increment value of the key containing the corresponding character in dictionary.
# Store the character as key in dictionary if not found.10
for char in morseoutput_str:
    if char in occurrence_dict:
        occurrence_dict[char] = occurrence_dict[char] + 1
    else:
        occurrence_dict[char] = 1

# Display header for output representation.
print("Character \t Occurrence")

# Display each key and value stored in occurrence dictionary.
for key, value in occurrence_dict.items():
    print(key, " \t "," \t "," \t ", value)

# Notify the occurrence of unmentioned characters.
print("Rest of the characters have 0 occurence.")