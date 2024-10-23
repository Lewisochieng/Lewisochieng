def reverse_integer(n):
    # Convert the integer to a string and reverse it, handling the negative sign if present
    if n < 0:
        reversed_num = int('-' + str(abs(n))[::-1])
    else:
        reversed_num = int(str(n)[::-1])
    return reversed_num

# Get input from the user
user_input = int(input("Please enter an integer: ").strip())

# Reverse the integer
reversed_result = reverse_integer(user_input)

# Output the result
print("Reversed integer:", reversed_result)
