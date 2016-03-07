import random
from time import sleep


class NumberGame:
    def __init__(self, usr_name, difficulty=1):
        self.usr_name = usr_name
        self.difficulty = difficulty
        self.high_number = self._high_number(self.difficulty)
        self.com_number = self._com_number(self.high_number)

    def _high_number(self, difficulty):
        high_number = difficulty * 20
        return high_number

    def _com_number(self, high_number):
        com_num = random.randint(1, high_number)
        return com_num

    def increase_difficulty(self, difficulty):
        new_difficulty = difficulty + 1
        return new_difficulty

    def check_win(self, guess):
        high_num = self.high_number
        com_num = self.com_number
        try:
            if 1 <= guess <= high_num:
                if guess > com_num:
                    return 'Too high.'
                elif guess < com_num:
                    return 'Too low.'
                elif guess == com_num:
                    return 'Way to go!'
            else:
                return 'Invalid Input.'
        except TypeError:
            return 'Please enter a NUMBER.'


def get_name():
    usr_name = input('What is your name?\n')
    return usr_name


def greeting(usr_name, high_num):
    print('Hello {}!\nI am thinking of a number between 1 and {}.'.format(usr_name, high_num))


def get_guess():
    try:
        guess = int(input('Take a guess.\n'))
        return guess
    except ValueError:
        pass


def game_loop(usr_name, com_num):
    guess_count = 0
    while guess_count < 6:
        guess = get_guess()
        print(game.check_win(guess))
        if game.check_win(guess) == 'Way to go!':
            return 'You guessed it in {} tries!'.format(guess_count)
        elif game.check_win(guess) != 'Invalid Input.':
            guess_count += 1
    print('Thanks for playing {}, but my number was {}'.format(usr_name, com_num))


def main():
    usr_name = get_name()
    global game
    game = NumberGame(usr_name)
    high_num = game.high_number
    greeting(usr_name, high_num)
    game_loop(usr_name, game.com_number)


if __name__ == '__main__':
    main()
