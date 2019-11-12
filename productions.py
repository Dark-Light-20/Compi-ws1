class Production1():
    """
    It can be: 'P', 'F', 'T', 'E', 'OR', 'ER', 'EL1', 'OL'
    """
    def __init__(self, production_type):
        # for OR ==> s1 -> char ['<','>','<=',...]
        self.s1 = None
        self.production_type = production_type

class Production2():
    """
    It can be: 'F_L', 'T_L', 'E_L', 'ER_L', 'OL2_L', 'OL_L'
    """
    def __init__(self, production_type):
        self.h1 = None
        self.s1 = None
        self.production_type = production_type

class Operation():
    """
    It can be: 'LogOr', 'logAnd', 'Sum', 'Less', 'Mul', 'Div', 'Pot'
    """
    def __init__(self, operation_type):
        self.h1 = None
        self.s2 = None
        self.s3 = None
        self.operation_type = operation_type

class Result():
    def __init__(self):
        self.s3 = None

class Comp():
    def __init__(self, comparator):
        self.h1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None
        self.comparator = comparator