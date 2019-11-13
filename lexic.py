class I():
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "I ("+str(self.value)+")"

    def __repr__(self):
        return "I ("+str(self.value)+")"

def lexicAnalysis(sequence):
    operators=['+','-','*','/','^','(',')','&','|','<','>','!','=']
    lexicSequence=[]
    available=False     # available -> to push an 'I'
    available2=False    # validate: (a '=' already analyzed after other operator) or (double logic operator)
    # instance of variables for substr the numbers:
    num1 = -1
    num2 = 0

    for pos, char in enumerate(sequence):   # create a tuple (pos, char) of sequence
        if char.isnumeric():
            if available == False:
                available=True
                num1=pos
        elif char in operators:
            if available:
                num = int(str(sequence[num1:pos]))  #get substr -> number
                i = I(num)  # instance class 'I' with atribute number
                lexicSequence.append(i)
                available=False
            if available2:
                available2=False
                continue
            if char == '<':
                if pos < len(sequence)-1 and sequence[pos+1] == '=':
                    lexicSequence.append("<=")
                    available2=True
                    continue
            elif char == '>':
                if pos < len(sequence)-1 and sequence[pos+1] == '=':
                    lexicSequence.append(">=")
                    available2=True
                    continue
            elif char == '!':
                if pos < len(sequence)-1 and sequence[pos+1] == '=':
                    lexicSequence.append("!=")
                    available2=True
                    continue
                else:
                    return error(pos, char)
            elif char == '=':
                if pos < len(sequence)-1 and sequence[pos+1] == '=':
                    lexicSequence.append("==")
                    available2=True
                    continue
                else:
                    return error(pos, char)        
            elif char == '|':
                if pos < len(sequence)-1 and sequence[pos+1] == '|':
                    lexicSequence.append("||")
                    available2=True
                    continue
                else:
                    return error(pos, char)     
            elif char == '&':
                if pos < len(sequence)-1 and sequence[pos+1] == '&':
                    lexicSequence.append("&&")
                    available2=True
                    continue
                else:
                    return error(pos, char)        
            
            lexicSequence.append(char)
        else:
            return error(pos, char)

        num2=pos

    if available:   # validation if last element in sequence is 'I'
        num2+=1
        num = int(str(sequence[num1:num2]))
        i = I(num)
        lexicSequence.append(i)
    
    lexicSequence.append("$")   # end of sequence char
    
    return lexicSequence

def error(pos, char):
    print("Lexic Error!!! Extrange Character found at "+str(pos)+": "+char)
    return None