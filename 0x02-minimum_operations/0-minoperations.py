def minOperations(n):
    if n == 1:
        return 0
    
    operations = 0
    clipboard = 1
    
    for i in range(2, n + 1):
        if n % i == 0:
            clipboard = i
            operations += 2
            break
    
    while n > 1:
        n //= clipboard
        operations += clipboard
    
    return operations

# Example usage:
n = 9
result = minOperations(n)
print(f"Number of operations for n={n}: {result}")

