import random
from collections import Counter

#from words import word_lis
'''def get_word():
    word= random.choice(word_list)
    return word.upper()'''

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 9
    print("Lets play Hang man.")
    print(display_hangman(tries))
    print("\n")
    word_list = list(word)
    completion_list = list(word_completion)
    while tries >= 0:
        print(completion_list)
        guess = input("Please Guess a Letter").upper()
        print(display_hangman(tries))
        if len(guess) !=1:
            print("Please Type a Letter")
            continue
        if guess in word:
            if guess in guessed_letters:
                print("you guessed it already")
            else:
                print("You guessed the letter",guess)
                index = word_list.index(guess)
                completion_list[index] = guess
                guessed_letters.append(guess)
                print(guessed_letters)
                if(Counter(guessed_letters) == Counter(word_list)):
                    print("you guessed it")
                    break
                else:
                    tries = tries -1
                    continue
        else:
            print(guess,"is not in the word")
            tries = tries-1
            continue
    if(Counter(guessed_letters) == Counter(word_list)):
        print("you guessed it")
    else:
        print("RIP")
        display_hangman(tries)
    again = input("do you want to play again(y/n)").upper()
    if(again == "Y"):
        main()
    else:
        exit()
        
def display_hangman(tries):
    stages= ["""

                --------
                |      |
                |      o
                |      \\|/
                |       |
                |       /\
                |
                |
                |
                |
                |
    
            """,
            """
                --------
                |      |
                |      o
                |      \\|/
                |       |
                |       /
                |
                |
                |
                |
                |
            """,
            """
                 --------
                |      |
                |      o
                |      \\|/
                |       |
                |       
                |
                |
                |
                |
                |
            """,
            """
                 --------
                |      |
                |      o
                |      \\|/
                |       
                |   
                |
                |
                |
                |
                |
            """,
            """
                 --------
                |      |
                |      o
                |      \\|
                |       
                |   
                |
                |
                |
                |
                |
            """,
            """
                 --------
                |      |
                |      o
                |      \\
                |       
                |       
                |
                |
                |
                |
                |
            """,
            """
                 --------
                |      |
                |      o
                |      \
                |       
                |       
                |
                |
                |
                |
                |
            """,
            """
                 --------
                |      |
                |      o
                |      
                |       
                |       
                |
                |
                |
                |
                |
            """,
            """
                 --------
                |      |
                |      
                |      
                |       
                |
                |
                |
                |
                |
                |
            """,
            """
                 --------
                |      
                |      
                |      
                |       
                |       
                |
                |
                |
                |
                |
            """
    ]
    return stages[tries]


def main():
    print("hi")
    word_listed = "Ant","Bus","Duck","Bird","Magic","Tatter"
    word= random.choice(word_listed)
    play(word.upper())

if __name__ == "__main__":
   main()


        
