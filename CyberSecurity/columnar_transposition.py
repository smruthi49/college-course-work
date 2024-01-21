import math

def CTEncrypt(plaintext, key):
    
    encrypted = ""
    index = 0
    
    length = len(plaintext)
    text_list = list(plaintext)
    key_list = sorted(list(key))
    
    col = len(key)
    row = int(math.ceil(length / col))
    
    fill_null = int((row * col) - length)
    text_list.extend('_' * fill_null)
    
    matrix = [text_list[i: i + col] for i in range(0, len(text_list), col)]
    
    for _ in range(col):
        curr_idx = key.index(key_list[index])
        encrypted += ''.join([row[curr_idx] for row in matrix])
        index += 1
        
    return encrypted.replace('_', '')

def CTDecrypt(encoded_text, key):   
    
    decrypted = ""
    
    index = 0
    
    text_index = 0
    length = len(encoded_text)
    text_list = list(encoded_text)
    
    col = len(key)
    row = int(math.ceil(length / col))
    key_list = sorted(list(key))
    
    decrypt_matrix = []
    for _ in range(row):
        decrypt_matrix += [[None] * col]
    
    for _ in range(col):
        curr_idx = key.index(key_list[index])
        
        for j in range(row):
            decrypt_matrix[j][curr_idx] = text_list[text_index]
            text_index += 1
        index += 1
        
    try :
        decrypted = ''.join(sum(decrypt_matrix, []))
    except TypeError:
        raise TypeError("This program cannot decrypt you text")
    
    null_count = decrypted.count('_')
    
    if null_count > 0:
        return decrypted[: -null_count]
    
    return decrypted

    