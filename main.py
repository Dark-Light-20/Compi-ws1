from lexic import lexicAnalysis
from syntax import syntaxAnalysis

"""
Taller 2 - Reconocimiento y ejecución de Secuencia Aritmetica-Logica-Relacional
Analisis Lexico y Sintactico con atributos

Presentado por:

Sebastian Alexander Diaz Paz
Juan Esteban Castro Guerrero
Peter D'Loise Chicaiza Cortez
Juan Sebastian Cardona Narvaez
Sergio Gomez Duque
"""

#expression="(25*8/7^(8-9)+5)<=(85)&&8+(45/8)!=8||54>8&&(54<5)"
expression=input("Type a logic-arithmetic expression: ")

print(expression)
print("----------------")
result=lexicAnalysis(expression)

if result is not None:
    print("Lexic sequence= "+str(result))
    print("----------------")
    analysis=syntaxAnalysis()
    analysis.loop(result)
    print("----------------")