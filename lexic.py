def lexicAnalysis(sequence):
    operators=['+','-','*','/','^','(',')','&','|','<','>','<=','>=','!','=']
    lexicSequence=[]
    available=False     # available -> to push an "I"
    
    for pos, char in enumerate(sequence):   # create a tuple (pos, char) of sequence
        if char.isnumeric():
            available=True
        elif char in operators:
            if available:
                lexicSequence.append("I")
                available=False
            lexicSequence.append(char)
        else:
            print("Error! Extrange Character found at "+str(pos)+": "+char)
            return None

    if available:   # validation if last element in sequence is "I"
        lexicSequence.append("I")
    
    lexicSequence.append("$")   # end of sequence char
    
    return lexicSequence

