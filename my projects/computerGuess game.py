import random

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    #Using this loop the computer will guess the number until we tell it its correct
    while feedback != 'c':
        guess =random.randint(low, high)
        feedback = input(f"Is {guess} high(h) or low(l) or correct(c) : ")
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1
        
    print(f"Yaay computer guessed your number {guess} correctly!!!")
    

computerGuess(10) #this number can be any number depending on the range you want