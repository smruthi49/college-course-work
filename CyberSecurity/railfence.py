
def RailFenceEncrypt(plaintext, key):
    
    rail = [['\n' for i  in range(len(plaintext))] for j in range(key)]
    
    direction_down = False
    row, col = 0,0
    
    for i in range(len(plaintext)):
        if row == 0 or row == key-1:
            direction_down = not direction_down
        
        rail[row][col] = plaintext[i]
        col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
            
    result = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    
    return ''.join(result)

def RailFenceDecrypt(encoded_text, key):
    
    rail = [['\n' for i  in range(len(encoded_text))] for j in range(key)]
    
    direction_down = None
    row, col = 0,0
    for i in range(len(encoded_text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
            
        rail[row][col] = '*'
        col += 1
        
        if direction_down:
            row += 1
        else :
            row -= 1
            
    index = 0
    for i in range(key):
        for j in range(len(encoded_text)):
            if rail[i][j] == '*' and index < len(encoded_text):
                rail[i][j] = encoded_text[index]
                index += 1
    
    result = []
    row, col = 0,0
    
    for i in range(len(encoded_text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
            
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
            
        if direction_down:
            row += 1
        else:
            row -= 1
            
    return ''.join(result)