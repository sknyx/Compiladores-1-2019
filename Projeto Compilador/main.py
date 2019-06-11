from parser import Parser
from symbolTable import SymbolTable

def read_file(file_name): 
    with open(file_name) as file:
        data = file.read()
    return data


def main():
        test = read_file("input3.txt")
        try:
            parser = Parser(test) 

            result = parser.parseProgram()

            symbolTable = SymbolTable(None)

            result.Evaluate(symbolTable)

        except ValueError as err:
            print(err)


main()
