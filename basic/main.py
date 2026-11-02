from operations import add, subtract, multiply, divide

a = 33
b = 3

sum_result = add(a, b)
difference_result = subtract(a, b)
product_result = multiply(a, b)
quotient_result = divide(a, b)

print("Calculation Results")
print(f"Addition: {a} + {b} = {sum_result}")
print(f"Subtraction: {a} - {b} number = {difference_result}")
print(f"Multiplication: {a} * {b} = {product_result}")
print(f"Division: {a} / {b} = {quotient_result}")