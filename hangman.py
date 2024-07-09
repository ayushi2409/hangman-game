import random

def choose_word():
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'cplusplus']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print("Try to guess a programming language name before the hangman is complete.")
    print(display_word(word, guessed_letters))
    
    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
        
        print(display_word(word, guessed_letters))
        
        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break
    
    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

hangman()