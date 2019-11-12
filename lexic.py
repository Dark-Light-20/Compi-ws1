def lexicAnalysis(sequence):
    operators=['+','-','*','/','^','(',')','&','|','<','>','!','=']
    lexicSequence=[]
    available=False     # available -> to push an "I"
    
    for pos, char in enumerate(sequence):   # create a tuple (pos, char) of sequence
        if char.isnumeric():
            available=True
        elif char in operators:
            if available:
                lexicSequence.append("I")
                available=False
            if char == '<':
                if pos < len(sequence)-1 and sequence[pos+1] == '=':
                    lexicSequence.append("<=")
                    continue
            elif char == '>':
                if pos < len(sequence)-1 and sequence[pos+1] == '=':
                    lexicSequence.append(">=")
                    continue
            elif char == '!':
                if pos < len(sequence)-1 and sequence[pos+1] == '=':
                    lexicSequence.append("!=")
                    continue
                else:
                    return error(pos, char)
            elif char == '=':
                if pos < len(sequence)-1 and sequence[pos+1] == '=':
                    lexicSequence.append("==")
                    continue
                else:
                    continue        
            lexicSequence.append(char)
        else:
            return error(pos, char)

    if available:   # validation if last element in sequence is "I"
        lexicSequence.append("I")
    
    lexicSequence.append("$")   # end of sequence char
    
    return lexicSequence

def error(pos, char):
    print("Lexic Error!!! Extrange Character found at "+str(pos)+": "+char)
    return None