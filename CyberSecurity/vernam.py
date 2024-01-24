

def VernamEncrypt(plaintext, key):
    
    plaintext = plaintext.lower()
    
    text_vector = [ord(i)-97 for i in plaintext]
    
    key_vector = []
    for i in range(len(text_vector)):
        key_vector.append(ord(key[i%len(key)])-97)
    
    new_vector = []
    
    for i in range(len(text_vector)):
        val = (text_vector[i] + key_vector[i]) % 26
        new_vector.append(val)
    
    
    return "".join([chr(i+97) for i in new_vector])



def VernamDecrypt(encrypted_text, key):
    
    encrypted_text = encrypted_text.lower()
    
    text_vector = [ord(i)-97 for i in encrypted_text]
    
    key_vector = []
    for i in range(len(text_vector)):
        key_vector.append(ord(key[i%len(key)])-97)
    
    new_vector = []
    
    for i in range(len(text_vector)):
        val = (text_vector[i] - key_vector[i]) % 26
        new_vector.append(val)
    
    
    return "".join([chr(i+97) for i in new_vector])

