
def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise TypeError("Both num and divisor must be numeric")
    
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))  # Expected: True
print(check_divisibility(7, 3))   # Expected: False

