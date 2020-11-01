"""Hangman program takes random word from WORD_LIST and separates it into
list of letters.  Rest of explanation is under playGame() method because that
is where most of the program runs.  Program loops in main() until user enters
'n' to stop it"""

import random

WORDS_LIST = ['assassinate', 'terminate', 'dougie', 'obama', 'barack', 'kitten',
              'waitress', 'basement', 'instigate', 'lmfao', 'brother',
              'inferior', 'german', 'flock', 'goose', 'hydroxide', 'apoxy',
              'shell']


class HangMan:
    """
    This class allows allows users to play the hangman game

    Attributes
    ----------
    finalWord       Word that is randomly chosen that user will have to guess
    letterList      List of letters of final word

    Methods
    --------
    getWord         Randomly selects word from WORDS_LIST
    separateLetters Separates self.finalWord into letters
    playGame        Contains all code to actually play the hangman game
    """

    def __init__(self):
        self.finalWord = ''
        self.letterList = []

    def getWord(self):
        """
        Gets random value between 0 and the length of WORD_LIST to index WORD_LIST
        Calls self.separateLetters
        :return:
        No return statement
        """
        wordListIndex = random.randint(0, (len(WORDS_LIST) - 1))
        self.finalWord = WORDS_LIST[wordListIndex]
        self.seperateLetters()

    def seperateLetters(self):
        """
        Separates letters in finalWord
        :return:
        No return statement
        """
        for letter in self.finalWord:
            self.letterList.append(letter)

    def playGame(self):
        """
        Method makes a local list of same length as self.letterList.
        Appends blank spaces to wordList, will be printed later to show user
        their progress and what letter is where.  Defines count variable to
        count how many times user has guessed wrong.  While loop begins, asks
        user for input.  If input in self.letterList, iterates over list, gets index,
        replaces '_' in local list with letter at same index.  Does opposite
        with self.letterList, removes letter and inserts underscore, had to
        do this to make program run correctly or duplicate letters would not be
        removed.  Prints letter that is correct, progress on word thus far.
        If there are no more underscores in wordList, user wins game, while
        loop exited to main.

        If user does not guess correctly, 1 is added to count, if count is 6
        user is told that they lost and loop is exited.  TypeError exception
        caught here.  tells user how many wrong guesses they have left."""
        wordList = []
        for n in range(len(self.letterList)):
            wordList.append("_")  # Adds blank spaces to wordList
        print("Your word is %d letters." % len(wordList))

        count = 0  # Used to count number of attempts
        while True:
            userGuess = input("Enter a letter here: ")
            if userGuess in self.letterList:  # Checks if guess is in letterList
                for letter in self.letterList:
                    if letter == userGuess:
                        index = self.letterList.index(letter)  # Gets index of letter
                        self.letterList.pop(index)  # Removes letter at index
                        self.letterList.insert(index, "_")  # Adds '_' at index
                        wordList.pop(index)  # Removes underscore at index
                        wordList.insert(index, userGuess)  # Adds userGuess at index
                print("That's right! %c is correct!" % userGuess)
                print("Here is your progress: \n")
                string = ''
                for char in wordList:  # Prints string from wordList nicely
                    string += char
                print(string)
                if "_" not in wordList:
                    print("Congrats! You got it! Your word is %s" % string)
                    break
            else:
                count += 1
                if count == 6:
                    print("That's all! Your word was %s" % self.finalWord)
                    break
                try:  # Handles TypeError
                    print("Oops! letter %c was not correct!" % userGuess)
                except TypeError:
                    print("Please only input one letter at a time!")
                print("Here is your progress: \n")
                string = ''
                for char in wordList:
                    string += char
                print(string)
                print("You have %d more tries!" % (6 - count))


def main():
    """
    Runs until loop breaks.  Makes object of HangMan class, calls two of
    its methods.  Asks user if they would like to play again once they have
    won or lost the game
    :return:
    """
    while True:
        play = HangMan()
        play.getWord()
        play.playGame()
        goAgain = input("Would you like to play again? (y / n) ")
        if goAgain == 'n':
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()


