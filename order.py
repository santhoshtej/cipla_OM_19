def reverse_number(n):
    reversed_num = int(str(abs(n))[::-1])
    return -reversed_num if n < 0 else reversed_num

# Example usage
num = 12345
print(reverse_number(num))  # Output: 54321