#**************************************  Snake-Water-Gun Game *********************************************************

print("Are your interested this Game! if your answer is YES then start the Game Begain\n ")
name = input("Please Enter your name : ")

import random
list = ["S", "W", "G"]

chance = 10
number_of_chance = 0
computer_point = 0
your_point = 0

print("\t\t\t\t Sanke Water Gun\n\n")
print("S for Snake\n W for Water\n G for Gun\n")

while number_of_chance<chance:
    _input = input("Snake, Water, Gun : ")
    _random = random.choice(list)
    
    if _input == _random:
        print("TIE!!! Both are O points\n")

    # if user enter "S"
    elif _input == "S" and _random == "W":
        your_point = your_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("Snake Ne Pani Pee Liya! Your are Win 1 point\n")
        print(f"computer point are {computer_point} and your point are {your_point}\n") 

    elif _input == "S" and _random == "G":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("Sanke ko Goli Lag Gayi Hai! Your are Loss 1 point\n")
        print(f"computer point are {computer_point} and your point are {your_point}\n") 
    
    # if user enter "W"
    elif _input == "W" and _random == "G":
        your_point = your_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print(" Pani Goli Se Paar Ho Gaya! Your are Win 1 point\n")
        print(f"computer point are {computer_point} and your point are {your_point}\n") 

    elif _input == "W" and _random == "S":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print(f"Snake Ne Pani Pee Liya! Your are Loss 1 point\n")
        print(f"computer point are {computer_point} and your point are {your_point}\n") 

     # if user enter "G"
    elif _input == "G" and _random == "S":
        your_point = your_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print(" Snake Ko Goli Lag Gayi Hai! Your are Win 1 point\n")
        print(f"computer point are {computer_point} and your point are {your_point}\n") 

    elif _input == "G" and _random == "W":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print(f"Pani Goli Se Paar Ho Gaya! Your are Loss 1 point\n")
        print(f"computer point are {computer_point} and your point are {your_point}\n") 


    else:
        print("Your are Wrong input\n")

    number_of_chance = number_of_chance + 1
    print(f"{chance - number_of_chance} is left out of {chance} Chance\n")    

print("Game Over!!!")

if computer_point > your_point:
    print("Computer WIN!!  and You Loose")
elif computer_point < your_point:
    print("You WIN!!  and Computer Loose")
else:
    print("Tie ! No Result")    

print(f"your points are {your_point} and Computer points are {computer_point}")
    