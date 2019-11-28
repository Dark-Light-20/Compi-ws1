from lexic import I

productions=[')','P','F_L','F','T_L','T','E_L','E','OR','ER_L','ER','OL2_L','EL1','OL_L','OL']

class syntaxAnalysis():
    def __init__(self):
        self.stack = []
        self.stack.append(0)
        self.stack.append("OL")
        self.i=0

    def loop(self, sequence):
        while(self.i<len(sequence)):
            """
            it must be another way fck XD
            """

            element = sequence[self.i]

            if len(self.stack) > 0:
                top=self.stack[-1]
            else:
                top = ''

            if top not in(productions):
                result = self.validateTop()

                if element == '$' and isinstance(result, str):
                    return "Sequence Accepted!!!"

                if result:
                    continue

            if isinstance(element, I):
                if top == ")":
                    break
                elif top == "P":
                    self.stack.pop()
                    self.stack[self.stack[len(self.stack)-1]]=str(element.value)
                    self.stack.pop()
                elif top == "F_L":
                    break
                elif top == "F":
                    self.six()
                elif top == "T_L":
                    break
                elif top == "T":
                    self.four()
                elif top == "E_L":
                    break
                elif top == "E":
                    self.one()
                elif top == "OR":
                    break
                elif top == "ER_L":
                    break
                elif top == "ER":
                    self.thirteen()
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    self.eleven()
                elif top == "OL_L":
                    break
                elif top == "OL":
                    self.nine()
                elif top == '':
                    break
            elif element == '+':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.two(element)
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    break
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '-':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.two(element)
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    break
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '*':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.five(element)
                elif top == "T":
                    break
                elif top == "E_L":
                    break
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    break
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '/':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.five(element)
                elif top == "T":
                    break
                elif top == "E_L":
                    break
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    break
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '^':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.seven()
                elif top == "F":
                    break
                elif top == "T_L":
                    break
                elif top == "T":
                    break
                elif top == "E_L":
                    break
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    break
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '(':
                if top == ")":
                    break
                elif top == "P":
                    self.eight()
                elif top == "F_L":
                    break
                elif top == "F":
                    self.six()
                elif top == "T_L":
                    break
                elif top == "T":
                    self.four()
                elif top == "E_L":
                    break
                elif top == "E":
                    self.one()
                elif top == "OR":
                    break
                elif top == "ER_L":
                    break
                elif top == "ER":
                    self.thirteen()
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    self.eleven()
                elif top == "OL_L":
                    break
                elif top == "OL":
                    self.nine()
                elif top == '':
                    break
            elif element == ')':
                if top == ")":
                    self.stack.pop()
                    value = self.stack.pop()
                    self.stack[self.stack.pop()] = value
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    self.three()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    self.three()
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    self.three()
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '&&':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    self.three()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    self.twelve()
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '||':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    self.three()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    self.three()
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    self.ten()
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '<':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    self.fifteen(element)
                elif top == "ER_L":
                    self.fourteen()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '>':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    self.fifteen(element)
                elif top == "ER_L":
                    self.fourteen()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '<=':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    self.fifteen(element)
                elif top == "ER_L":
                    self.fourteen()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '>=':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    self.fifteen(element)
                elif top == "ER_L":
                    self.fourteen()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '!=':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    self.fifteen(element)
                elif top == "ER_L":
                    self.fourteen()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '=':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    self.fifteen(element)
                elif top == "ER_L":
                    self.fourteen()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    break
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    break
                elif top == "OL":
                    break
                elif top == '':
                    break
            elif element == '$':
                if top == ")":
                    break
                elif top == "P":
                    break
                elif top == "F_L":
                    self.three()
                elif top == "F":
                    break
                elif top == "T_L":
                    self.three()
                elif top == "T":
                    break
                elif top == "E_L":
                    self.three()
                elif top == "E":
                    break
                elif top == "OR":
                    break
                elif top == "ER_L":
                    self.three()
                elif top == "ER":
                    break
                elif top == "OL2_L":
                    self.three()
                elif top == "EL1":
                    break
                elif top == "OL_L":
                    self.three()
                elif top == "OL":
                    break
                elif top == '':
                    return "Sequence Accepted!!!"
        
            self.i+=1
        
        return self.error(top, element)
            
    def one(self):
        self.stack.pop()
        self.stack.append('#')
        self.stack.append("E_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append("T")
        self.i-=1

    def two(self, element):
        self.stack.pop()
        value = self.stack.pop()
        self.stack.append('#')
        self.stack.append("E_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append(value)
        self.stack.append('#')
        if element == '+':
            self.stack.append('SUM')
        else:
            self.stack.append('RES')
        self.stack.append(len(self.stack)-2)
        self.stack.append("T")
    
    def three(self):
        self.stack.pop()
        value = self.stack.pop()
        self.stack[self.stack[len(self.stack)-1]]=value
        self.stack.pop()
        self.i-=1

    def four(self):
        self.stack.pop()
        self.stack.append('#')
        self.stack.append("T_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append("F")
        self.i-=1

    def five(self, element):
        self.stack.pop()
        value = self.stack.pop()
        self.stack.append('#')
        self.stack.append("T_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append(value)
        self.stack.append('#')
        if element == '*':
            self.stack.append('MUL')
        else:
            self.stack.append('DIV')
        self.stack.append(len(self.stack)-2)
        self.stack.append("F")
    
    def six(self):
        self.stack.pop()
        self.stack.append('#')
        self.stack.append("F_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append("P")
        self.i-=1
        
    def seven(self):
        self.stack.pop()
        value = self.stack.pop()
        self.stack.append('#')
        self.stack.append("F_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append(value)
        self.stack.append('#')
        self.stack.append('POT')
        self.stack.append(len(self.stack)-2)
        self.stack.append("P")
    
    def eight(self):    # trabajar
        self.stack.pop()
        self.stack.append('#')
        self.stack.append(")")
        self.stack.append(len(self.stack)-2)
        self.stack.append("OL")

    def nine(self):
        self.stack.pop()
        self.stack[len(self.stack)-1]='#'
        self.stack.append("RESULT")
        self.stack.append(len(self.stack)-2)
        self.stack.append('#')
        self.stack.append("OL_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append("EL1")
        self.i-=1
    
    def ten(self):
        self.stack.pop()
        value = self.stack.pop()
        self.stack.append('#')
        self.stack.append("OL_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append(value)
        self.stack.append('#')
        self.stack.append('LOG|')
        self.stack.append(len(self.stack)-2)
        self.stack.append("EL1")
    
    def eleven(self):
        self.stack.pop()
        self.stack.append('#')
        self.stack.append("OL2_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append("ER")
        self.i-=1
    
    def twelve(self):
        self.stack.pop()
        value = self.stack.pop()
        self.stack.append('#')
        self.stack.append("OL2_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append(value)
        self.stack.append('#')
        self.stack.append('LOG&')
        self.stack.append(len(self.stack)-2)
        self.stack.append("ER")

    def thirteen(self):
        self.stack.pop()
        self.stack.append('#')
        self.stack.append("ER_L")
        self.stack.append(len(self.stack)-2)
        self.stack.append("E")
        self.i-=1
    
    def fourteen(self):
        self.stack.pop()
        value = self.stack.pop()
        self.stack.append('#')
        self.stack.append(value)
        self.stack.append('#')
        self.stack.append('COMP')
        self.stack.append(len(self.stack)-2)
        self.stack.append("E")
        self.stack.append(len(self.stack)-6)
        self.stack.append("OR")
        self.i-=1

    def fifteen(self, element):
        self.stack.pop()
        if isinstance(element, I):
            self.stack[self.stack[len(self.stack)-1]]=str(element.value)
        else:
            self.stack[self.stack[len(self.stack)-1]]=str(element)
        self.stack.pop()
    
    def error(self, top, element):
        if top == ')':
            return "Syntax Error!!! closing parenthesis expected but ' "+element+" ' arrived at position: "+str(self.i)
        
        elif top == 'P':
            return "Syntax Error!!! identifier or opening parenthesis expected but ' "+element+" ' arrived at position: "+str(self.i)
        
        elif top == 'F_L':
            return "Syntax Error!!! operator, closing parenthesis or end of string expected but ' "+element+" ' arrived at position: "+str(self.i)

        elif top == 'F':
            return "Syntax Error!!! identifier or opening parenthesis expected but ' "+element+" ' arrived at position: "+str(self.i)

        elif top == 'T_L':
            return "Syntax Error!!! operators (+,-,*,/,&&,||,<,>,=,<=,>=,!=,==), closing parenthesis or end of string expected but ' "+element+" ' arrived at position: "+str(self.i)

        elif top == 'T':
            return "Syntax Error!!! identifier or opening parenthesis expected but ' "+element+" ' arrived at position: "+str(self.i)
        
        elif top == 'E_L':
            return "Syntax Error!!! operators (+,-,&&,||,<,>,=,<=,>=,!=,==), closing parenthesis expected or end of string expected  but ' "+element+" ' arrived at position: "+str(self.i)

        elif top == 'T':
            return "Syntax Error!!! identifier or opening parenthesis expected but ' "+element+" ' arrived at position: "+str(self.i)

        elif top == 'OR':
            return "Syntax Error!!! comparison operator expected but ' "+element+" ' arrived at position: "+str(self.i)
        
        elif top == 'ER_L':
            return "Syntax Error!!! closing parenthesis, logical/comparison operator or end of string expected but ' "+element+" ' arrived at position: "+str(self.i)

        elif top == 'ER':
            return "Syntax Error!!! identifier or opening parenthesis expected but ' "+element+" ' arrived at position: "+str(self.i)

        elif top == 'OL2_L':
            return "Syntax Error!!! logical operator, closing parenthesis or end of string expected but ' "+element+" ' arrived at position: "+str(self.i)
        
        elif top == 'EL1':
            return "Syntax Error!!! identifier or opening parenthesis expected but ' "+element+" ' arrived at position: "+str(self.i)

        elif top == 'OL_L':
            return "Syntax Error!!!  closing parenthesis, || operator or end of string expected but ' "+element+" ' arrived at position: "+str(self.i)  
        
        elif top == 'OL':
            return "Syntax Error!!! identifier or opening parenthesis expected but ' "+element+" ' arrived at position: "+str(self.i)
        
        elif top == '':
            return "Syntax Error!!! end of sequence expected but ' "+element+" ' arrived at position: "+str(self.i)

        #return "Syntax Error!!! It was expected ' "+top+" ' and it arrived ' "+element+" ', at position: "+str(self.i)

    def validateTop(self):
        operator = self.stack.pop()
        if operator == 'RESULT':
            value = self.stack.pop()
            print('----------')
            print(value)
            print('----------')
            return value
        value2 = self.stack.pop()
        value1 = self.stack.pop()

        if operator == 'COMP':
            relationalop = self.stack.pop()
            if relationalop == '<':
                value = value1<value2
            elif relationalop == '>':
                value = value1>value2
            elif relationalop == '<=':
                value = value1<=value2
            elif relationalop == '>=':
                value = value1>=value2
            elif relationalop == '==':
                value = value1 == value2
            elif relationalop == '!=':
                value = value1 != value2
        elif operator == 'SUM':
            value = int(value1) + int(value2)
        elif operator == 'RES':
            value = int(value1) - int(value2)
        elif operator == 'MUL':
            value = int(value1) * int(value2)
        elif operator == 'DIV':
            value = int(value1) // int(value2)
        elif operator == 'LOG|':
            value = value1 or value2
        elif operator == 'LOG&':
            value = value1 and value2

        self.stack[self.stack[len(self.stack)-1]] = str(value)
        self.stack.pop()
        return True
        
        """
        if self.stack[len(self.stack)-1] == 'MUL':
            self.stack.pop()
            value2 = self.stack.pop()
            value1 = self.stack.pop()
            value = int(value1) * int(value2)
            self.stack[self.stack[len(self.stack)-1]] = str(value)
            self.stack.pop()
            return True
        """
