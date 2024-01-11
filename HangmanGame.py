def hangman():
    words = ["hondai", "tata", "toyto", "mercedes", "jaguar", "rangerover", "fiat"]
    word = random.choice(words)
    guessed_letter =[]
    attempts = 6

    print("Let's play Hangman!")
    print("The word has", len(word),"letters.")

    while attempts > 0 :
        print("\n Attempt left:",attempts)
        guessed_word = " "
        for letter in word:
            if letter in guessed_letter:
                guessed_word += letter
            else:
                guessed_word += "_"
        print("Guessed word:", guessed_word)

        if guessed_word == word:
            print("Congratulation, you guessed the word!")
            break
        guess = input("Guess a letter:").lower()

        if guess in guessed_letter:
            print("You already guessed that letter. Try again.")
        elif len(guess) !=1 :
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter valid letter")
        else:
            guessed_letter.append(guess)
            if guess not in word:
                attempts -= 1
                print("Wrong guess !")
    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was", word)
hangman()

