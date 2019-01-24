import word_bank as wb

class Hangman():
    def __init__(self):
        self.word_obj = wb.WordBank()
        self._word, self.length = self.word_obj.word
        self._dashes = []
        self.wrong_count = 0
        self.guesses = []

    @property
    def word(self):
        return self._word


    @property
    def dashes(self):
        for dash in range(self.length):
            self._dashes.append("_")
        return self._dashes

    #Thinking about it, I can truncate it to search the word and compare with the
    #user_char, but that is still O(n), instead of O(2n), which is the same thing
    #In other words. Eh. Works and doesn't matter TOO much, since it's all O(n) anyways
    def find_dups_indices(self, ch):
        return [i for i, ltr in enumerate(self.word) if ltr == ch]

    def add_to_result(self, user_char):
        dups = self.find_dups_indices(user_char)
        if user_char in self.word:
            for n in dups:
                self._dashes[n] = user_char
        else:
            self.wrong_count += 1
            print("Sorry, that isn't in the word")
            print("Wrong count: {}".format(self.wrong_count))
        self.guesses.append(user_char)

    def print_result(self):
        print(" ".join(self._dashes))

    def main_loop(self):
        self.dashes
        done = False
        while not done:
            print("Guess the word!")
            self.print_result()
            user_in = input("Please enter a character (will take first character entered) \n> ")
            if not user_in:
                print("Please enter a valid character")
                continue
            elif user_in in self.guesses:
                print("You already guessed that! Try again")
                continue
            self.add_to_result(user_in[0]) 
            print("You have guessed: {}".format(self.guesses))
            if self.wrong_count >= 10:
                done = True
                print("Sorry, you lose. The word was '{}'".format(self.word))
            elif "_" not in self._dashes:
                self.print_result()
                print("You guessed the word!")
                print("Goodbye")
                done = True




if __name__ == "__main__":
    h = Hangman()
    h.main_loop()
