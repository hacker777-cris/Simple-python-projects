import random
print("\n               WELCOME TO THE GUESSING GAME")
print("\n               created by H4CK3R_777")
options = ['1.NEW GAME','2.LOAD GAME','3.QUIT GAME']
fileName = 'storage.txt'
write = 'w'
append = 'a'
read = 'r'


for x in range(len(options)) :
    print(options[x])

userOption = input("PLEASE PICK AN OPTION FROM THE ABOVE: ")
if userOption == '1':
    def guess(x):
        randomNumber = random.randint(1, x)
        guess = 0
        while guess != randomNumber:
            guess = int(input(f"Guess a number between 1 and {x} : "))
            if guess < randomNumber:
                print("Sorry the number you guessed is too low!!!")
            elif guess > randomNumber:
                print("Sorry the number you guessed is too high !!!")
        print(f"Yaay, You won you guessed {x} correctly!!!")
        with open('storage.txt', 'a') as file:
            file.write(str(guess) + ',')
        
    guess(10) #this number can be any number

if userOption == '2':
    print("\n           BELOW ARE ALL OF YOUR PREVIOUS WINNING GUESSES")
    with open('storage.txt', 'r') as file:
        contents = file.read()
        print(contents)
elif userOption == '3':
    exit()

input("Press Enter to exit...")  

   





