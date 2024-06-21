#guess the number
import random
 
target = random.randint(1, 100) 


while True:
    userChoice = input("guess the target or Quit : ")
    if(userChoice == "Quit"):
        break


    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct guess !!")
        break
    elif(userChoice < target):
        print("your number was too small.Take a bigger guess..")
    else:
        ("your number was too big.Take a small guess..")    

print("-----GAME OVER-----")