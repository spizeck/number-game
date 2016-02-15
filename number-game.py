import random


class NumberGame:
    """
    Generates the high number
    """

    def __init__(self, highNumber, playerName):
        self.highNumber = highNumber
        self.playerName = playerName
        self.com_number = random.randint(1, self.highNumber)
        self.check_win = False
        self.play_again = 'n'
        self.guess = None
        self.guess_count = 1

    def start(self):
        """
        Starts the game
        """
        self.check_win = False
        self.play_again = 'n'
        self.guess_count = 1
        self.gameLoop()

    def gameLoop(self):
        """
        Loops the game
        """
        print('Well {}, I am thinking of a number between 1 and {}.'.format(self.playerName, self.highNumber))
        # 6 valid guesses allowed
        while self.guess is not self.com_number and self.guess_count < 6:
            # Loop in case of invalid input
            while True:
                # Get input and check for valid input
                try:
                    self.guess = int(input('Take a guess.\n'))
                    if 1 <= self.guess <= self.highNumber:
                        break
                    else:
                        print('Invalid input.')
                except ValueError:
                    print('Invalid input')
            # Add 1 to guess count
            self.guess_count += 1
            # Give user clues
            if self.guess < self.com_number:
                print('Too low.')
            elif self.guess > self.com_number:
                print('Too high.')
        # set check_win flag to True
        self.check_win = True
        self.playAgain()

    def checkWin(self):
        """
        Returns value for play_again loop in main()
        """
        return self.check_win

    def playAgain(self):
        """
        Check if they want to play again.
        """
        self.play_again = input('Do you want to play again?\n(y/n)')
        if self.play_again != 'y':
            return False
        else:
            return True


def highScore():
    """
    Prints the top 3 to be added later
    """
    pass


def main():
    difficulty = 1
    highNumber = 20 * difficulty
    playerName = input('Hello! What is your name?\n')
    game = NumberGame(highNumber, playerName)
    game.start()
    while game.playAgain() is True:
        if game.checkWin() is True:
            difficulty += 1
        else:
            difficulty = 1
        highNumber = 20 * difficulty
        game = NumberGame(highNumber, playerName)
        game.start()
    print('Thanks for playing!')


# Executes code for testing
if __name__ == "__main__":
    main()
