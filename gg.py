secret_word = "giraffe "

guess = " "
guess_count = 0 
guess_limit = 3
out_of_guesses = false 


while guess != secret_word and not (out_of_guesses) :

    guess = input(" enter guess: ")
    guess_count += 1


print("you win!!!!")
