#Rehan Javaid rj3dxu
bounds = list(range(1, 101))
print("Think of a number between 1 and 100 and I'll guess it.")
guesses = int(input("How many guesses do I get? "))

while guesses != 0:
    if (max(bounds)) != (min(bounds)):
        num_guess = (max(bounds) + min(bounds))//2
        num_guess = str(num_guess)
        response = input("Is the number higher, lower, or the same as "+ num_guess + " ?: ")
        num_guess = int(num_guess)
        if response == "same":
            print("I won!")
            break
        elif response == "higher":
            bounds = bounds[bounds.index(num_guess + 1) : len(bounds)]
            guesses-= 1
            continue
        elif response == "lower":
            bounds = bounds[0 : bounds.index(num_guess)]
            guesses -= 1
            continue
    elif min(bounds) == max(bounds):
        if (max(bounds)+1) - (min(bounds)) == 1:
            number_between = (min(bounds))
            response2 = input("Is the number higher, lower, or the same as " + str(number_between) + " ?: ")
            if response2 == "lower":
                print("Wait; how can it be both higher than " + str(min(bounds)-1) + " and lower than " + str(max(bounds)) + "?")
            elif response2 == "higher":
                print("Wait; how can it be both higher than " + str(min(bounds)) + " and lower than " + str(max(bounds)+1) + "?")
            elif response2 == "same":
                print ("I won!")
        break
if guesses < 1:
    actual_num = int(input("I lost; what was the answer? "))
    if actual_num < min(bounds):
        print("That can't be; you said it was higher than " + str(min(bounds)-1) + "!")
    elif actual_num > max(bounds):
        print("That can't be; you said it was lower than " + str(max(bounds)+1) + "!")
    elif min(bounds) <= actual_num <= max(bounds):
        print("Well played!")


