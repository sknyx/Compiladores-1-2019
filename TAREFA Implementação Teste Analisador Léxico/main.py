
Delimiters = [' ', ',', ' ;', ':', '(', ')']

Operators = ['+', '-', '*', '/', '=',':=']

Keywords = ['Program','Var', 'real', 'Const','Begin','Read','Write','End.']

lineNum = 0;
e = 0
filename = "code.txt"
file = open(filename, "r")

#----------------------------------------
def isDelimiter(code):
  if code in Delimiters:
    return True
  else:
    return False

def isOperator(code):
  if code in Operators:
    return True
  else:
    return False

def isIdentifier(code):
  if code[0].isnumeric() or isDelimiter(code[0]):
    return False
  else:
    return True

def isKeyword(code):
  if code in Keywords:
    return True
  else:
    return False
#----------------------------------------

for line in file:
  lineNum = lineNum + 1
  code_field = line.split(" ")

  for i in code_field:
    if (isKeyword(i) or isIdentifier(i) or isDelimiter(i) or isOperator(i) or i.isnumeric() or isIdentifier(i)) == False:
      print("Erro na linha ", lineNum, "!")
      print("Erro -> ",i)
      e = 1;

if e != 1:
  print("\nO código está lexicalmente correto!")

file.close()
