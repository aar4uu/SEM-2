import random

class Rock_paper_scissors:
    def __init__(self, rounds):  # Corrected constructor name from _init_ to __init__
        self.user_wins = 0
        self.computer_wins = 0
        self.total_rounds = rounds
        self.current_round = 0

    def get_user_choice(self):
        choice = input("Enter rock, paper or scissors: ").lower()
        while choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.")
            choice = input("Enter rock, paper, or scissors: ").lower()
        return choice
    
    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def find_winner(self, user_choice, comp_choice):
        print(f"Your choice: {user_choice}, Computer's choice: {comp_choice}")
        
        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            print("You win this round!")
            self.user_wins += 1
        else:
            print("Computer wins this round!")
            self.computer_wins += 1

    def check_winners(self):
        if self.user_wins > self.computer_wins:
            print(f"You win the game (Your Wins: {self.user_wins}, Computer Wins: {self.computer_wins})")
        elif self.computer_wins > self.user_wins:
            print(f"Computer wins the game (Your Wins: {self.user_wins}, Computer Wins: {self.computer_wins})")
        else:
            print(f"It's a tie! (Your Wins: {self.user_wins}, Computer Wins: {self.computer_wins})")

    def play_game(self):
        while self.current_round < self.total_rounds:
            print(f"Round {self.current_round + 1}:")
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            self.find_winner(user_choice, computer_choice)
            self.current_round += 1

        self.check_winners()  # Final winner check after all rounds

# Start the game
rounds = int(input("Enter the number of rounds to play: "))
game = Rock_paper_scissors(rounds)
game.play_game()
