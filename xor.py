#Given the string "label" XOR each character with the integer 13. Convert these integers back to a string.

data = "label"
flag = ''

for c in data:
    flag += chr(ord(c) ^ 13)

print('crypto{{{}}}'.format(flag))
