def lexicAnalysis(sequence):
    operators=['+','-','*','/','^','(',')']
    syntaxsequence=[]
    i=0
    available=False
    for char in sequence:
        if char.isnumeric():
            available=True
        elif char in operators:
            if available:
                syntaxsequence.append("I")
                available=False
            syntaxsequence.append(char)
        else:
            print("Error! Extrange Character found at "+str(i)+": "+char)
            return None
        i+=1
    a=sequence[len(sequence)-1:]
    if a.isnumeric():
        syntaxsequence.append("I")
    syntaxsequence.append("$") # end of sequence char
    return syntaxsequence

