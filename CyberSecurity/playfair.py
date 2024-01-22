def removeSpaces(plaintext):
    text = ""
    
    for i in plaintext:
        if i != ' ':
            text += i
    return text

def LetterFill(plaintext):
    n = len(plaintext)
    
    if n%2 == 0:
        #split to two letters
        for i in range(0,n,2):
            if plaintext[i] == plaintext[i+1]:
                new_text = plaintext[0:i+1] + 'x' + plaintext[i+1:]
                new_text = LetterFill(new_text)
                break
            else:
                new_text = plaintext
    else:
        
        for i in range(0,n-1,2):
            if plaintext[i] == plaintext[i+1]:
                new_text = plaintext[0:i+1] + 'x' + plaintext[i+1:]
                new_text = LetterFill(new_text)
                break
            else:
                new_text = plaintext
    return new_text
                
def Digraph(plaintext):
    Digraph = []
    group = 0
    
    for i in range(2,len(plaintext), 2):
        Digraph.append(plaintext[group:i])
        group = i
    Digraph.append(plaintext[group:]+'z')
    return Digraph


#list of alphabets
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generateMatrix(key, l):
    key_letters = []
    
    #append all the letters in the key to key_letters
    for i in key:
        if i not in key_letters:
            key_letters.append(i)
            
    elements = []
    #append all the letters in the key_letters to elements
    for i in key_letters:
        if i not in elements:
            elements.append(i)
            
    #append remaining letters in l to elements
    for i in l:
        if i not in elements:
            elements.append(i)
            
    # build the matrix
    matrix  = []
    while elements != []:
        matrix.append(elements[0:5])
        elements = elements[5:]
    
    return matrix

def search(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i,j
            
def RowEncrypt(matrix, x1,y1,x2,y2):
    char1 , char2 = '', ''
    
    if y1 == 4:
        char1 = matrix[x1][0]
    else:
        char1 = matrix[x1][y1+1]
    
    if  y2 == 4:
        char2 = matrix[x2][0]
    else:
        char2 = matrix[x2][y2+1]
    
    return char1, char2

def ColEncrypt(matrix, x1,y1,x2,y2):
    
    char1, char2 = '',''
    
    if x1 == 4:
        char1 = matrix[0][y1]
    else:
        char1 = matrix[x1+1][y1]
    
    if  x2 == 4:
        char2 = matrix[0][y2]
    else:
        char2 = matrix[x2+1][y2]
        
    return char1, char2
    
def RectangleEncrypt(matrix, x1,y1,x2,y2):
    char1, char2 = '',''
    
    char1 = matrix[x1][y2]
    char2 = matrix[x2][y1]
    
    return char1, char2

def PlayFairEncrypt(plaintext, key):
    key = key.lower()
    plaintext = plaintext.lower()
    encrypted = ""

        
    text_list = Digraph(LetterFill(removeSpaces(plaintext)))
    matrix = generateMatrix(key, l)
    
    
    for i in range (0, len(text_list)):
        c1, c2 = 0,0
        x1,y1 = search(matrix, text_list[i][0])
        x2,y2 = search(matrix, text_list[i][1])
        
        #same row
        if x1 == x2:
            c1,c2 = RowEncrypt(matrix, x1,y1,x2,y2)
        #same column
        elif y1 == y2:
            c1,c2 = ColEncrypt(matrix, x1,y1,x2,y2)
        #different row and column
        else:
            c1,c2 = RectangleEncrypt(matrix, x1,y1,x2,y2)
        
        encrypted += c1 + c2
        
    return encrypted


def RowDecrypt(matrix, x1,y1,x2,y2):
    char1 , char2 = '', ''
    
    if y1 == 0:
        char1 = matrix[x1][4]
    else:
        char1 = matrix[x1][y1-1]
    
    if  y2 == 0:
        char2 = matrix[x2][4]
    else:
        char2 = matrix[x2][y2-1]
    
    return char1, char2

def ColDecrypt(matrix, x1,y1,x2,y2):
    
    char1, char2 = '',''
    
    if x1 == 0:
        char1 = matrix[4][y1]
    else:
        char1 = matrix[x1-1][y1]
    
    if  x2 == 0:
        char2 = matrix[4][y2]
    else:
        char2 = matrix[x2-1][y2]
        
    return char1, char2

def PlayFairDecrypt(encrypted_text, key):
    key = key.lower()
    encrypted_text = encrypted_text.lower()
    decrypted = ""
    
    text_list = Digraph(removeSpaces(encrypted_text))
    matrix = generateMatrix(key, l)
    
    for i in range (0, len(text_list)):
        c1, c2 = 0,0
        x1,y1 = search(matrix, text_list[i][0])
        x2,y2 = search(matrix, text_list[i][1])
        
        #same row
        if x1 == x2:
            c1,c2 = RowDecrypt(matrix, x1,y1,x2,y2)
        #same column
        elif y1 == y2:
            c1,c2 = ColDecrypt(matrix, x1,y1,x2,y2)
        #different row and column
        else:
            c1,c2 = RectangleEncrypt(matrix, x1,y1,x2,y2)
        
        decrypted += c1 + c2
        
    return decrypted