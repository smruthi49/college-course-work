
def get_key(plaintext, key):
    key = key.upper()
    
    if len(plaintext) == len(key):
        return key
    else :
        for i in range(len(plaintext) - len(key)):
            key += key[i % len(key)]
    return key

def VigenereEncrypt( plaintext, key):
    plaintext = plaintext.upper()
    encrypted = ""
    
    key = get_key(plaintext, key)
    
    for i in range(len(plaintext)):
        char = (ord(plaintext[i]) + ord(key[i])) % 26
        char += ord('A')
        encrypted += chr(char)
    return encrypted

def VigenereDecrypt( encoded_text, key):
    encoded_text = encoded_text.upper()
    decrypted = ""
    
    key = get_key(encoded_text, key)
    
    for i in range(len(encoded_text)):
        char = (ord(encoded_text[i]) - ord(key[i]) + 26) % 26
        char += ord('A')
        decrypted += chr(char)
    return decrypted
