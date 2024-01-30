def removeSpaces(plaintext):
    text = ""
    
    for i in plaintext:
        if i != ' ':
            text += i
    return text

def Digraph(plaintext):
    Digraph = []
    group = 0
    
    for i in range(2,len(plaintext), 2):
        Digraph.append(plaintext[group:i])
        group = i
    if len(plaintext[group:])%2 == 0:
        Digraph.append(plaintext[group:])
    else:
        Digraph.append(plaintext[group:]+'z')
    return Digraph

def MatrixMultiplication(vector, key):
    
    new_vector = [[0],[0]]
    
    for i in range(len(new_vector)):
        for j in range(len(new_vector[0])):
            for k in range(len(key)):
                new_vector[i][j] += key[i][k]*vector[k][j]
            new_vector[i][j] = new_vector[i][j]%26
            
            
    return new_vector

def HillCipherEncrypt(plaintext,key):
    encrypted = ""
    plaintext = plaintext.lower()
    
    graph = Digraph(removeSpaces(plaintext))
    
    text_vector = []
    for division in graph:
        
        text_vector.append([[ord(i)-96] for i in division])
    
    matrix = [[0] for i in range(2)]
    
    for vector in text_vector:
        temp = MatrixMultiplication(vector, key)
        
        encrypted += chr(temp[0][0]+96)
        encrypted += chr(temp[1][0]+96)
        
    return encrypted

def matrixInverse(matrix):
    determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    inverse = [[0,0],[0,0]]
    
    if determinant == 0:
        return "Matrix is not invertible"
    
    if determinant != 1:
        #we take the multiplicative inverse of the determinant
        for i in range(26):
            if determinant*i%26 == 1:
                determinant = i
                break
            
        inverse[0][0] = matrix[1][1]
        inverse[0][1] = -matrix[0][1]
        inverse[1][0] = -matrix[1][0]
        inverse[1][1] = matrix[0][0]    
        
        for i in range(len(inverse)):
            for j in range(len(inverse[0])):
                inverse[i][j] = inverse[i][j] * determinant
                inverse[i][j] = inverse[i][j]%26
        return inverse
    
    else:
        inverse[0][0] = matrix[1][1]
        inverse[0][1] = -matrix[0][1]
        inverse[1][0] = -matrix[1][0]
        inverse[1][1] = matrix[0][0]
        
        for i in range(len(inverse)):
            for j in range(len(inverse[0])):
                inverse[i][j] = inverse[i][j]/determinant
                inverse[i][j] = int(inverse[i][j]%26)
        return inverse

def HillCipherDecrypt(encrypted_text, key):
    
    decrypted = ""
    
    graph = Digraph(removeSpaces(encrypted_text))
    
    text_vector = []
    for division in graph:
        
        text_vector.append([[ord(i)-96] for i in division])
    
    matrix = [[0] for i in range(2)]
    key = matrixInverse(key)
    
    for vector in text_vector:
        temp = MatrixMultiplication(vector, key)
        
        decrypted += chr(temp[0][0]+96)
        decrypted += chr(temp[1][0]+96)
        
    return decrypted

    