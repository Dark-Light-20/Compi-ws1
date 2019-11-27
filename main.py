from lexic import lexicAnalysis
from syntax import syntaxAnalysis

expression="(25*8/7^(8-9)+5)<=(85)&&8+(45/8)!=8||54>8&&(54<5)"
#expression=input("Type a logic-arithmetic expression: ")

print(expression)
print("----------------")
result=lexicAnalysis(expression)

if result is not None:
    print(result)
    print("----------------")
    #analysis=syntaxAnalysis()
    #print(analysis.loop(result))
    print("----------------")