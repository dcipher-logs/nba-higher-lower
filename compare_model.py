import random
from logo import logo, or_logo

class StatsBrain:
    def __init__(self, data):
        self.data = data
        self.score = 0
        self.attempts = 0
        self.comparisons = 50
        self.number1 = random.randint(0, 550)
        self.number2 = random.randint(0, 550)
        if self.number1 == self.number2:
            self.number2 = random.randint(0,550)


    def still_comparisons(self):
        return self.attempts != 50


    def next_comparisons(self):
        while self.still_comparisons():
            self.attempts += 1
            self.comparisons -= 1
            self.number1 = random.randint(0, 550)
            self.number2 = random.randint(0, 550)
            if self.number1 == self.number2:
                self.number2 = random.randint(0, 550)
            player_a = self.data[self.number1]
            player_b = self.data[self.number2]
            print(logo)
            print(f"Player A: {player_a.nbaplayer}")
            print(or_logo)
            print(f"Player B: {player_b.nbaplayer}")
            answer = input("Who has MORE Points? (Type A, B, or Tie): ").lower()
            print("\n" * 20)
            is_correct = self.check_answer(answer, player_a, player_b)
            if is_correct:
                self.score += 1
                print(f"You got it right! Your current score: {self.score}/{self.attempts}")
            else:
                print(f"Not Quite! Your current score: {self.score}/{self.attempts}")

    def check_answer(self, u_answer, player_a_, player_b_):
        if player_a_.points > player_b_.points:
            print(f"{player_a_.nbaplayer} has more points this season: {player_a_.points}")
            return u_answer == 'a'
        elif player_a_.points == player_b_.points:
            print(f"It's a TIE (how rare)! Both have {player_a_.points} points this season.")
            return u_answer == 'tie'
        else:
            print(f"{player_b_.nbaplayer} has more points this season: {player_b_.points}")
            return u_answer == 'b'