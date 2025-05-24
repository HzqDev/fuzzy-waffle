import random
import time 
while True:
    r = random.randint(0,100)
    guess = None
    attempts = 0
    print("welcome to number guessing game")
    time.sleep(2)
    print("i am thinking of a number between 1 to 100")
    time.sleep(2)
    while guess != r:
        guess = int(input("take a guess\t"))
        if ((guess>0) and (guess<100)):
            attempts +=1
            time.sleep(2)
            if guess > r:
                print("guessed high\t")
            elif guess < r:
                print("guessed low\t")
            else:
                print(f"Correct\n you guess it in {attempts} attempts")
        else:
            print("the number is between 0 to 100 if you didnt understood")
    answer = input("do you want to play again (y/n)")
    if answer=="n":
        print("thanks for playing")
        break        