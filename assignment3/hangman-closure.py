def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        for ch in secret_word:
            if ch in guesses:
                display += ch
            else:
                display += "_"
        print(display)
        return all(ch in guesses for ch in secret_word)

    return hangman_closure


secret = input("Enter the secret word: ")
guess_letter = make_hangman(secret)

done = False
while not done:
    letter = input("Guess a letter: ")
    done = guess_letter(letter)

print("You got it!")
