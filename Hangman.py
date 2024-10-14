import random

words = ("coconut", "pineapple","apple", "orange" ,"banana")

#dictionary of key:()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               
               1:(" o ",
                  "   ",
                  "   "),
               
               2:("  o ",
                  " | ",
                  "   "),
               3:(" o ",
                 " /| ",
                  "   "),
               
               4:("  o ",
                 " /|\ ",
                  "   "),
               
               5:("  o ",
                 " /|\ ",
                  " /  "),
               
               6:("  o ",
                 " /|\ ",
                  " / \ ")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
     print(line)
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
    answer = random.choice(words)
    hint = ["_"] * len(answer)
        if len(guess) !=1 or not guess.isalpha:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
            
        guessed_letters.add(guess)
        if guess in answer:
             for i in range(len(answer)):
              if answer[i] == guess:
                  hint[i] = guess
        else:
            wrong_guesses += 1
            
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lose")
            is_running = False
            

if __name__ == "__main__":
    main()

 