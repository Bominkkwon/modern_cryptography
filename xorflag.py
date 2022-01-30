# We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character. Given the string "label" XOR each character with the integer 13. Convert these integers back to a string and submit the flag as codecrypto{new_string}.
data = "label"
flag = ''

for c in data:
    flag += chr(ord(c) ^ 13)

print('crypto{{{}}}'.format(flag))