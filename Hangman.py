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

 