from art import logo
import os

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def power(n1, n2):
  return n1 ** n2

def square_root(n1, n2):
  return n1 ** (1/n2)

operations = {"+" : add,
          "-" : subtract,
          "*" : multiply,
          "/" : divide,
          "**" : power,
          "v" : square_root
             }

def calculator():
  print(logo)
  num1 = float(input("Type the first number: \n"))
  
  for symbols in operations:
    print(symbols)
  
  should_continue = True
  while should_continue:
      operation_symbol = input("Pick an operation: \n")
      if operation_symbol not in operations:
        print("Invalid data")
        break
      next_number = float(input("Type the next number: \n"))
      calculation_function = operations[operation_symbol]
      result = calculation_function(num1, next_number)
      result_printed = f"{num1} {operation_symbol} {next_number} = {result}"
      print(result_printed)

      next_operation = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: \n")
      if next_operation == "y":
        num1 = result
      else:
        should_continue = False
        os.system("cls")
        calculator()
        
calculator()