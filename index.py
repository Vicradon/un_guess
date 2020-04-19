from random import randrange


def level_details(mode):
    if mode == 'easy':
        return {'guesses': 6, 'range': 10}
    elif mode == 'medium':
        return {'guesses': 4, 'range': 20}
    else:
        return {'guesses': 3, 'range': 50}


def guess_block(mode):
    guesses = level_details(mode)['guesses']
    guess_range = level_details(mode)['range']
    guess = randrange(0, guess_range)

    while guesses > 0:
        user_input = int(input(f"Enter a number between 0 and {guess_range}: "))
        print(f"\n{user_input} - {guess}\n")
        print(user_input == guess)
      
        if user_input != guess:
            guesses -= 1
            if guesses == 0:
                print("You have exhausted your trials. You lose")
                replay()
            else:
                print(f"Wrong guess. You have {guesses} guesses left")
        else:
            print("You guessed correctly! You win!")
            replay()


def replay():
    replay_value = input("Do you want to play again? \n(yes or no):")
    while replay_value != 'yes' and replay_value != 'no':
        replay_value = input(
            "Please, enter 'yes' or 'no'. \nDo you want to play again?: ")
        if replay_value == 'yes':
            play_game()
        elif replay_value == 'no':
            print("Thanks for playing. See ya!")
            break


def play_game():
    mode = input(
        "Please, enter your desired mode \n(easy or medium or hard): ")
    while mode != 'easy' and mode != 'medium' and mode != 'hard':
        mode = input(
            "Please, enter a right response. Either 'easy', 'medium' or 'hard'. Must be lowercase: ")
        if mode == 'easy' or mode == 'medium' or mode == 'hard':
            break
    guess_block(mode)


play_game()