import random

class Dealer:
    def __init__(self):
        self.current_card = random.randint(1, 13)
        self.previous_card = 0
        self.guess = ""
        self.score = 0
    def draw_card(self):
        """
        Returns a random card, 1-13
        """
        self.previous_card = self.current_card
        self.current_card = random.randint(1, 13)
    def ask_user(self):
        """
        Determines the user's guess
        """
        self.guess = input("Higher or lower? [h/l] ").lower()
        while self.guess not in ("h", "l"):
            print("\nError: please enter \'h\' or \'l\'")
            self.guess = input("Higher or lower? [h/l] ").lower()
    def can_play(self):
        """
        Determines whether the player can still play, then asks if they would like to play again
        """
        return (self.score > 0)
    def get_points(self):
        """
        Returns points based on the user's guess
        """
        if self.guess == "h" and self.current_card >= self.previous_card:
            return 100
        elif self.guess == "h" and self.current_card < self.previous_card:
            return -75
        elif self.guess == "l" and self.current_card <= self.previous_card:
            return 100
        else:
            return -75
