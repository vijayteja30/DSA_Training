"""
Recursion:
    1. Direct Recursion
    2. Indirect Recursion
    3. Tail Recurion
    4. Non-Tail Recursion
    
"""

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# print(f"Factorial of 5: {factorial(5)}")  # Example usage

num=1
for i in range(5):
    num *= (i + 1) # num = num*(i+1)
    # print(f"Factorial of {i + 1}: {num}")  # Iterative approach for comparison

def factorial_while(n):
    num = 1
    while True:
        if n == 0 or n == 1:
            break
        num *= n
        n -= 1
    return num

print(f"Factorial of 5 using while: {factorial_while(0)}")


def print_recursion_1(n):
    """
    Print numbers from n to 0 using recursion.
    
    :param n: Non-negative integer
    """
    if n < 0:
        return
    print(n)
    print_recursion_1(n - 1)

print(f"Printing numbers: {print_recursion_1(5)}")  # 5 4 3 2 1 0


def print_recursion_2(n):
    """
    Print numbers from n to 0 using recursion.
    
    :param n: Non-negative integer
    """
    if n < 0:
        return
    print_recursion_2(n - 1)
    print(n)

print(f"Printing numbers: {print_recursion_2(5)}")  # 0 1 2 3 4 5


# Indirect recursion examples
# Indirect recursion occurs when a function calls another function, which in turn calls the first function
# This can lead to a cycle of function calls until a base case is reached.

def indirect_recursion_a(n):
    """
    Indirect recursion example A.
    
    :param n: Non-negative integer
    """
    if n > 0:
        print(f"Indirect Recursion A: {n}")
        indirect_recursion_b(n - 1) # Calls indirect_recursion_b
def indirect_recursion_b(n):
    """
    Indirect recursion example B.
    
    :param n: Non-negative integer
    """
    if n > 0:
        print(f"Indirect Recursion B: {n}")
        indirect_recursion_a(n - 1) # Calls indirect_recursion_a
# Example usage of indirect recursion
indirect_recursion_a(5)



def tail_sum(n, accumulator=0):
    if n == 0:
        return accumulator
    return tail_sum(n - 1, accumulator + n) # Rec
