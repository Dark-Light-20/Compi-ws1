from lexic import lexicAnalysis
from syntax import syntaxAnalysis

expression="25^(8*2)-98/(45+5)-7"
#expression=input("Type a arithmetic expression: ")
result=lexicAnalysis(expression)
if result is not None:
    print(expression)
    print("----------------")
    print(result)
    print("----------------")
    analysis=syntaxAnalysis()
    print(analysis.cycle(result))
    