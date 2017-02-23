import sys
import math

def addition(x,y):
   return x + y

def subtraction(x,y):
   return x - y

def multiplication(x,y):
   return x * y

def division(x,y):
   return x / y

def power(x,y):
   return x ** y

def negate(x):
   return -x

def square(x):
   return x ** 2

def squareroot(x):
   return math.sqrt(x)

def logarithm(x):
   return math.log(x)

binary = {
   "+" : addition,
   "-" : subtraction,
   "*" : multiplication,
   "/" : division,
   "**" : power,
}

unary = {
   "n" : negate,
   "s" : square,
   "r" : squareroot,
   "l" : logarithm,
}

def operate(stack, token):
   if token in binary:
      y = stack.pop()
      x = stack.pop()
      result = binary[token](x,y)
      stack.append(result)
   elif token in unary:
      x = stack.pop()
      result = unary[token](x)
      stack.append(result)
   else:
      stack.append(float(token))
   

def main():
   stack = []
   line = sys.stdin.readline()
   while line:
      tokens = line.split()
      for tok in tokens:
         operate(stack, tok)
      print ">", " ".join(map(str, stack))
      line = sys.stdin.readline()
      

if __name__ == "__main__":
   main()
