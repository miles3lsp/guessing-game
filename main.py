import random

class GuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 99)
        self.score = 10
        self.is_running = True

    def check_even_odd(self):
        if self.secret_number % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd ")

    def process_guess(self, user_input):
        if user_input == 'exit':
            self.is_running = False
            return

        if user_input == 'is the number even':
            self.check_even_odd()
            return

        try:
            guess = int(user_input)
            if guess == self.secret_number:
                print("You won")
                print(f"Your score {self.score}")
                self.is_running = False
            else:
                print("You lose")
                self.score -= 1
        except ValueError:
            print("Invalid input. Please enter a number, 'is the number even' or 'exit'.")

    def start(self):
        print("The game is started")
        while self.is_running:
            user_input = input("Guess the number: ").strip()
            self.process_guess(user_input)


if __name__ == "__main__":
    game = GuessingGame()
    game.start()