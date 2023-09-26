def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product

print(factorial(5))
print(factorial(2))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 24










# def factorial(n):
#     product = 1
#     print(f"at the start product is {product}")
#     while n > 0:
#         n -= 1
#         print(f"we multiply {product} by {n}")
#         product *= n
#         print(f"we get {product}")
      
#     return product

# print(f"""
#  Running: factorial(5)
# Expected: 120
#   Actual: {factorial(5)}
# """)
