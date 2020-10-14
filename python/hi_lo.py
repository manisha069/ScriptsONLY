low = 1
high = 1000
print("Hey Computer ! Guess a number between 1-1000")
input("Press ENTER to start => ")
count = 0
while high != low:
    # print(f"\tGuessing i the range of {low} to {high}")
    if count == 10:
        print("Sorry, I have exhausted number of chances, you need to improve your analytical skills !\n"
        "Better luck next time:)") 
        break
    count += 1 # (Watch video#75 to learn augmented asignments)
    guess = low + ((high - low) // 2 )
    high_low = input(f"My guess is {guess}.\n" 
    "Press 'h' if I need to guess higher,\n"
    "'l' if I need to guess lower or\n"
    "'c' if my guess is correct : ").casefold()
    if (high_low == 'c'):
        print(f"Hurrey! I won the game in {count} times.")
        break
    elif (high_low == 'h'):
        # Need to guess higher, the low end of the range becomes one greater than the guess.
        low = guess + 1
    elif (high_low == 'l'):
        # Need to guess lower, the high end of the range becomes one less than the guess.
        high = guess - 1
    else:
        print("Wrong input !")
else:
    print(f"Your guess must be {high}. I guessed it in 10 times")   



