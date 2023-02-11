import time
import random
import words_list


class Game():

    def __init__(self):
        self.words = words_list.return_list()
        self.still_playing = True
        self.lives = 8
        self.known_letters = []

    def run(self):

        while self.still_playing:

            self.welcome()

            input_player = self.player_input()

            if input_player == "QUIT":
                self.still_playing = False
                self.end()
                break

            elif input_player == "Start":

                self.play()

                choice_play_again = input("Wanna play again? (y/n): ")

                if choice_play_again.lower() == "n":
                    self.still_playing = False
                    self.end()
                    break
                else:
                    self.reset_all_varaibles()

    def player_input(self):

        self.start_or_play = input("Type 'start' to play or 'end' to stop: ")

        if self.start_or_play == "start":

            return "Start"

        elif self.start_or_play == "end":
            return "QUIT"
        else:
            print("\nType either start or stop dipshit!")
            return self.player_input()

    def play(self):

        word = random.choice(self.words)
        star_word = "*" * len(word)
        while self.lives != 0:

            if star_word == word:
                print(f"The word was {word}.")
                print("You won!")
                return "Won"

            print(f"Your word is : {star_word}")
            print(f"Your lives left are : {self.lives}")

            player_letter = input("Enter your guess (only one letter): ")

            if len(player_letter) != 1:
                print("\nYou didnt follow the rules (only one letter was allowed dipshit!)."
                      "\nI am taking one of your lives suck urself!")
                self.lives = self.lives - 1
                continue

            if player_letter in word:
                star_word = ""

                for i in range(0, len(word)):

                    if player_letter == word[i] or word[i] in self.known_letters:
                        star_word = star_word + word[i]
                    else:
                        star_word = star_word + "*"

                # updating the list

                self.known_letters.append(player_letter)

                continue

            self.lives = self.lives - 1

        print(f"The word was {word}!")
        print("You suck ew hahha fuck you!")

        return "Lost"

    def welcome(self):
        print("***\tWelcome to HANGMAN!\t***")

    def end(self):
        print("***\tTHANKS FOR PLAYING\t***")

    def reset_all_varaibles(self):
        self.lives = 8
        self.known_letters.clear()


# GAME LOGIC

# if will give _ _ _ _ _
# and the player has to guess
if __name__ == '__main__':
    Game().run()
