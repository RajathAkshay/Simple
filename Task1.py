# Rajath Akshay Vanikul (29498724)

#  Building a Simple Morse Code Decoder


# Create a Morse dictionary and define morse code using binary digits for each English alphabet and number(0 to 9).
# Display the Morse code representation as output.


# Create and define the morse code dictionary
# Keys - binary representation of morse code, Values - English alphabets and numbers
morse_dict = {'01': 'A', '1000': 'B', '1010':'C', '100':'D','0':'E','0010':'F',
              '110':'G','0000':'H','00':'I','0111':'J','101':'K','0100':'L',
              '11':'M','10':'N','111':'O','0110':'P','1101':'Q','010':'R',
              '000':'S','1':'T','001':'U','0001':'V','011':'W','1001':'X','1011':'Y','1100':'Z'
              ,' ':' ',
              '11111':'0','01111':'1','00111':'2','00011':'3','00001':'4','00000':'5',
              '10000':'6','11000':'7','11100':'8','11110':'9'}

# Display the header for representation.
print("Morse \t Character")

# Display each key and value stored in Morse code dictionary in legible vertical fashion.
for key,value in morse_dict.items():
    print(key,'  \t ',value)