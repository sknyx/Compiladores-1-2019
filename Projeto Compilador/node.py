from value import Value
from symbolTable import SymbolTable as SymbolTableClass
from id import Id


class Node():
    def __init__(self, value, children):
        self.id = Id.getNewId()
        self.value = value
        self.children = children

    def Evaluate(self, SymbolTable, whileFlag=0):
        pass


class BinOp(Node):
    def same_type(self, value1, value2):
        if (value1.type == value2.type):
            return True
        else:
            return False

    def Evaluate(self, SymbolTable, whileFlag=0, nodeId=None):
        value1_obj = self.children[0].Evaluate(SymbolTable, whileFlag)
        value2_obj = self.children[1].Evaluate(SymbolTable, whileFlag)
        value1 = value1_obj.getValue()
        value2 = value2_obj.getValue()
        if (self.value == "+"):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_sum = value1 + value2
            result = Value("int")
            result.setValue(value_sum)
            return result
        elif (self.value == "-"):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_sub = value1 - value2
            result = Value("int")
            result.setValue(value_sub)
            return result
        elif (self.value == "or"):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_or = value1 or value2
            result = Value("boolean")
            result.setValue(value_or)
            return result
        elif (self.value == "*"):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_mult = value1 * value2
            result = Value("int")
            result.setValue(value_mult)
            return result
        elif (self.value == "/"):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_div = value1 // value2
            result = Value("int")
            result.setValue(value_div)
            return result
        elif (self.value == "and"):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_and = value1 and value2
            result = Value("boolean")
            result.setValue(value_and)
            return result
        elif (self.value == ">"):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_bigger = value1 > value2
            result = Value("boolean")
            result.setValue(value_bigger)
            return result
        elif (self.value == "<"):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_smaller = value1 < value2
            result = Value("boolean")
            result.setValue(value_smaller)
            return result
        elif (self.value == "="):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_equal = value1 == value2
            result = Value("boolean")
            result.setValue(value_equal)
            return result
        elif (self.value == "!="):
            if not self.same_type(value1_obj, value2_obj):
                raise ValueError("Operands must be the same type")
            value_diff = value1 != value2
            result = Value("boolean")
            result.setValue(value_diff)
            return result
        else:
            return


class Assignment(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        name = self.children[0].Evaluate(SymbolTable, whileFlag).getValue()
        value = self.children[1].Evaluate(SymbolTable, whileFlag).getValue()
        SymbolTable.setSymbol(name, value)


class UnOp(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        value_obj = self.children[0].Evaluate(SymbolTable, whileFlag)
        value = value_obj.getValue()
        if (self.value == "-"):
            result = Value("int")
            result.setValue(value * -1)
            return result
        elif (self.value == "not"):
            if value_obj.type == "boolean":
                result = Value("boolean")
                result.setValue(not value)
                return result
            else:
                raise ValueError("Operand must be a boolean")
        else:
            return


class StrVal(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        value = Value("string")
        value.setValue(self.value)
        return value


class IntVal(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        value = Value("int")
        value.setValue(self.value)
        return value


class BoolVal(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        value = Value("boolean")
        value.setValue(self.value)
        return value


class Identifier(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        value = SymbolTable.getSymbol(self.value)
        return value


class NoOp(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        return None


class Statements(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        for child in self.children:
            child.Evaluate(SymbolTable, whileFlag)


class Print(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        value = self.children[0].Evaluate(SymbolTable, whileFlag)
        print(value.getValue())


class Read(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        result = input()
        value = Value("int")
        value.setValue(int(result))
        return value


class If(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        comp = self.children[0].Evaluate(SymbolTable, whileFlag, self.id)
        if (comp.value):
            self.children[1].Evaluate(SymbolTable, whileFlag)
        else:
            self.children[2].Evaluate(SymbolTable, whileFlag)


class While(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        comp = self.children[0]
        flag = 0
        while (comp.Evaluate(SymbolTable, flag, self.id).getValue()):
            self.children[1].Evaluate(SymbolTable, flag)
            flag = 1

class Program(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        SymbolTable.createSymbol(self.value, None)
        for i in range(len(self.children)):
            self.children[i].Evaluate(SymbolTable, whileFlag)


class VarDec(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        value1_obj = self.children[0].Evaluate(SymbolTable, whileFlag)
        value2_obj = self.children[1].Evaluate(SymbolTable, whileFlag)
        value1 = value1_obj.getValue()
        value2 = value2_obj.getValue()
        SymbolTable.createSymbol(value1, value2)


class MultiVarDec(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        for child in self.children:
            child.Evaluate(SymbolTable, whileFlag)


class FuncDec(Node): #declaração de função -> método de avaliação: criação 
    def Evaluate(self, SymbolTable, whileFlag=0):
        SymbolTable.createSymbol(self.value, "func")
        SymbolTable.setSymbol(self.value, self)


class Funcs(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        for func in self.children:
            func.Evaluate(SymbolTable, whileFlag)


class FuncCall(Node):
    def Evaluate(self, SymbolTable, whileFlag=0):
        func_name = self.value
        func_node = SymbolTable.getSymbol(func_name, "func").getValue()
        funcSymbolTable = SymbolTableClass(SymbolTable)
        var_dec = func_node.children[0]
        args = [x.children[0] for x in var_dec.children]
        func_node.children[0].Evaluate(funcSymbolTable, whileFlag)
        if (len(args) != len(self.children)):
            raise ValueError("Number of arguments must \
                              be the same as declaration")
        for i in range(len(args)):
            symbol = args[i].Evaluate(funcSymbolTable, whileFlag).getValue()
            symbol_type = funcSymbolTable.getSymbol(symbol).getType()
            value_obj = self.children[i].Evaluate(SymbolTable, whileFlag)
            if (symbol_type != value_obj.getType()):
                raise ValueError("Function argument must be \
                                   the same as declared")
            value = value_obj.getValue()
            funcSymbolTable.setSymbol(symbol, value)
        for i in range(1, len(func_node.children)):
            func_node.children[i].Evaluate(funcSymbolTable, whileFlag)
        result = funcSymbolTable.getSymbol(func_name)
        return result
