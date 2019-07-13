letter = "J"
tries = 3

def check_guess (guess, letter):
    if not guess.isalpha():
        print("Invalid")
        return False
    if letter == guess.upper():
        return True
    elif letter < guess.upper():
        print ("Your guess is High")
        return False
    else:
        print ("Your guess is Low")
        return False

def letter_guess():
    for i in range(tries):
        guess = input ("Enter your guess ")
        res = check_guess (guess, letter)
        if res:
            print ("Correct!")
            return True
    return False

result = letter_guess()
if result:
    print ("Congratulations")
else:
    print ("The answer was ",letter)
print ("GAME OVER!")