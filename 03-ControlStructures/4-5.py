plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha(): 
        char_code = ord(char)
        char_code += 1
        encrypted_char = chr(char_code)
    else:
        encrypted_char = char
    
    encrypted_text += encrypted_char

print(f"Encrypted text: {encrypted_text}")