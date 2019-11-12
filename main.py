from lexic import lexicAnalysis
from syntax import syntaxAnalysis

expression="(25*8/7^(8-9)+5)<(85)&8+(45/8)!8"
#expression=input("Type a logic-arithmetic expression: ")
result=lexicAnalysis(expression)
if result is not None:
    print(expression)
    print("----------------")
    print(result)
    print("----------------")
    analysis=syntaxAnalysis()
    print(analysis.loop(result))
    