#Write a program that takes an integer as input and returns an integer with 
reversed digit ordering
def reverse_integer(n):
    
    if n < 0:
        reversed_num = int('-' + str(abs(n))[::-1])
    else:
        reversed_num = int(str(n)[::-1])
    return reversed_num


user_input = int(input("Please enter an integer: ").strip())

reversed_result = reverse_integer(user_input)

print("Reversed integer:", reversed_result)
