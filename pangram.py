# Write a Python function to check whether a string is pangram or not.
def pangram(userInput):
    
    pangram = set()
    Alphabets = set('abcdefghijklmnopqrstuvwxyz')  

    for a in userInput:
        if a in Alphabets:
            pangram.add(a)  
            
    A = sorted(list(pangram))
    B = sorted(list(Alphabets))


    if A == B:
        
        print('Your word is a pangram!')
        
    else:
        
        print('Sorry, Your word is not a pangram.')
        
    print('Thank you!')  
    
print("Please enter a word to determine if it's a pangram:")
userInput = input().lower().strip()

Results = pangram(userInput)