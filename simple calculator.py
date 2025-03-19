
def add(x,y):
  return x+y
def subract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  if y!=0:
    return x/y
  else:
    return"error! division by zero."
def calculator():
  print("Simple calculator")
  print("Choose operator:")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")

  while True:
    choice =input("Enter choice (1/2/3/4):")

    if choice in ['1','2','3','4']:
      num1=float(input("Enter first number:"))
      num2=float(input("Enter second number:"))

      if choice=='1':
        print(f"The result is:{add(num1,num2)}")
      elif choice=='2':
        print(f"The result is:{subract(num1,num2)}")
      elif choice=='3':
        print(f"THE result is:{multiply(num1,num2)}")
      elif choice=='4':
        print(f"The result is:{divide(num1,num2)}")

      next_calculation=input("do you want to perfors another calculation?(yes/no):")
      if next_calculation.lower()!='yes':
        break
    else:
      print("invaild input")
    #Run the calculator
calculator()
