import random
playing=True
while playing:
    # List of predefined words
    words = ["python", "apple", "ocean", "tiger", "music"]

    # Randomly choose a word
    secret_word = random.choice(words)

    # Create blanks for the word
    guessed_word = ["_"] * len(secret_word)

    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6
    
    print("=== HANGMAN GAME ===")

    while incorrect_guesses < max_guesses and "_" in guessed_word:
        print("\nWord:", " ".join(guessed_word))
        print("Lives left ❤️   :", max_guesses - incorrect_guesses)
        print("Guessed letters:", ", ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if letter is in the word
        if guess in secret_word:
            print("Correct!")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Wrong guess!")
            incorrect_guesses += 1

    # Game result
    if "_" not in guessed_word:
        print("\n🎉Congratulations! 🎉You guessed the word:", secret_word)
    else:
        print("\n💀Game Over!💀")
        print("The word was:", secret_word)

    if not input("Play again?(y/n): ").lower() =="y":
        playing=False
print("Thanks for playing!")
