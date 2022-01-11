import operator

num1 = float(input("1st number: "))
operators = input("Operator: ")
num2 = float(input("2nd number: "))

def calculate(num1, num2, operators):
    print(operatorName[operators](num1, num2))

operatorName = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "%": operator.mod}
calculate(num1, num2, operators)
# add = calculate(num1, num2, operators)
# print(f"Answer is {add}")