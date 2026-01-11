import random

class GameEngine:
    def __init__(self, min_val=1, max_val=100):
        self.min_val = min_val
        self.max_val = max_val
        self.target = 0
        self.attempts = 0
        self.reset_game()

    def reset_game(self):
        self.target = random.randint(self.min_val, self.max_val)
        self.attempts = 0

    def check_guess(self, guess):
        """
        Checks the user's guess against the target.
        Returns: 'CORRECT', 'LOW', 'HIGH', or 'INVALID'
        """
        try:
            val = int(guess)
        except ValueError:
            return 'INVALID'

        self.attempts += 1
        
        if val == self.target:
            return 'CORRECT'
        elif val < self.target:
            return 'LOW'
        else:
            return 'HIGH'
