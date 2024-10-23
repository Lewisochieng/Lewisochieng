# Write a Python function that checks whether a word or phrase is palindrome or not.  

def IsPalindrome(userInput):
    
    reverseInput = userInput[::-1]
    print(reverseInput)

    if userInput == reverseInput:
        
        print('Your word is a pallindrome!')
        
    else:
        print('sorry, your word is not a palindrome!')
        
    print('Thank you!')

print('write a word to determine if it is a palindrome:')
userInput = input()

Palindrome = IsPalindrome(userInput)


        



    