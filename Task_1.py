# def factorial_loop(n):
#     if n < 0:
#         return "No Factorail for any negative number"
    
#     result = 1
#     for i in range(1,n+1):
#         result*=i
    
#     return result


def factorial_recursion(n):
    if n < 0:
        return "No Factorail for any negative number"
    if n == 0 or n ==1:
        return 1

    return n * factorial_recursion(n-1)



n = int(input("Enter any number to find its factorail: "))

print(f"Factorial of {n} is {factorial_recursion(n)}")