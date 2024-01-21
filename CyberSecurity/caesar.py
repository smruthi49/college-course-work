
def CaesarEncrypt(plaintext, shift):
    encrypted = ""
        
    for char in plaintext:
        if char == " ":
            encrypted += " "
        elif char.isupper():
            encrypted += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            encrypted += chr((ord(char) + shift - 97) % 26 + 97)
    return encrypted
    
def CaesarDecrypt(encoded_text, shift):
    decrypted = ""
    for char in encoded_text:
        if char == " ":
            decrypted += " "
        elif char.isupper():
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decrypted += chr((ord(char) - shift - 97) % 26 + 97)
            
    return decrypted

