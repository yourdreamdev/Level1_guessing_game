#guess random number within range
import random
correct_answer = random.randint(0, 20)
#correct_answer = 55

print("Welcome to the guessing game")
print("Guess a number between 0 and 20")

while True:
    try:   
        user_answer = int(input())
        if user_answer == correct_answer:
            print("correct")
            break
        else:
            print("wrong")
    except ValueError:
        print("NUMBERS ONLY")

#if user_answer == correct_answer:
    #print("correct")
#else:
    #print("error")