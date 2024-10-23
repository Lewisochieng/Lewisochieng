'''Write a program that accepts a string as input, capitalizes the first letter of each 
word in the string, and then returns the result string.'''


def capitalize_words(input_string):
    
    result = input_string.title()
    return result

user_input = input("Please enter a string: ").strip()

capitalized_string = capitalize_words(user_input)

print("Result:", capitalized_string)