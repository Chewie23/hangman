#Making a word bank module for the game to use
import random

class WordBank():
    def __init__(self):
        self.easy_words   = ["cat", "dog", "cow", "tree", "pig", "lion"]
        self.medium_words = ["jaguar", "army", "remote", "quiz", "lock"]
        self.hard_words   = ["giraffe", "rhythm", "gypsy", "sphynx", "pygmy"]
        self.my_word         = ""
        self.word_length  = 0
    
    def get_random_word(self, word_list):
        return word_list[ random.randrange( len(word_list) ) ]

    @property
    def word(self):
        user_in = input("""Do you want [E]asy, [M]edium or [H]ard words? ( Defaults to [M] )
> """
        )
        try:
            if user_in[0].lower() == "e":
                self.my_word = self.get_random_word(self.easy_words)
            elif user_in[0].lower() == "h":
                self.my_word = self.get_random_word(self.hard_words)
            else:
                self.my_word = self.get_random_word(self.medium_words)
        except IndexError:
            self.my_word = self.get_random_word(self.medium_words)
        self.word_length = len(self.my_word)
        return (self.my_word, self.word_length)

if __name__ == "__main__":
    my_word = WordBank()
    print (my_word.word)


