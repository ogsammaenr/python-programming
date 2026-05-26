import random


# ===== Oyun 1 ====
# Ana oyun yapısı
class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                print("it's a tie")

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


# ==== Oyun 2 ====
class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # 1. oyuncu kazanirsa
        if len(player1_word) > len(player2_word):
            return 1
        # 2. oyuncu kazanirsa
        elif len(player2_word) > len(player1_word):
            return 2
        # beraberlik
        return 0


# ==== Oyun 3 ====
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiouAEIOU"
        # kelimelerdeki sesli harfleri sayiyoruz
        vowels1 = len([char for char in player1_word if char in vowels])
        vowels2 = len([char for char in player2_word if char in vowels])

        if vowels1 > vowels2:
            return 1
        elif vowels2 > vowels1:
            return 2
        return 0


# ==== oyun 4 ====
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_moves = ["rock", "paper", "scissors"]
        p1_valid = player1_word in valid_moves
        p2_valid = player2_word in valid_moves

        # hatali girdi kontrolleri
        # ikisi de hatali ise 0
        if not p1_valid and not p2_valid:
            return 0
        # sadece p2 hatali degil ise 2
        if not p1_valid:
            return 2
        # sadece p1 hatali degil ise 1
        if not p2_valid:
            return 1

        # berabere ise 0 donduruyoruz
        if player1_word == player2_word:
            return 0

        # birinci oyuncu kazaniyor ise 1 kaybediyor ise 2 donduruyoruz
        return (
            1
            if (player1_word == "rock" and player2_word == "scissors")
            or (player1_word == "paper" and player2_word == "rock")
            or (player1_word == "scissors" and player2_word == "paper")
            else 2
        )


# Test Alanı
if __name__ == "__main__":
    p = WordGame(1)
    p.play()

    # ============================
    print("\n", "=" * 50, "\n")

    p = LongestWord(1)
    p.play()

    # ============================
    print("\n", "=" * 50, "\n")

    p = MostVowels(1)
    p.play()

    # ============================
    print("\n", "=" * 50, "\n")

    p = RockPaperScissors(1)
    p.play()

    # Çıktı: (girdiler = ['longword', '??', 'short', 'longsword', 'aaaa', 'baba', 'rock', 'paper'])
    #
    # Word game:
    # round 1
    # player1: longword
    # player2: ??
    # player 1 won
    # game over, wins:
    # player 1: 1
    # player 2: 0
    #
    # ==================================================
    #
    # Word game:
    # round 1
    # player1: short
    # player2: longsword
    # player 2 won
    # game over, wins:
    # player 1: 0
    # player 2: 1
    #
    # ==================================================
    #
    # Word game:
    # round 1
    # player1: aaaa
    # player2: baba
    # player 1 won
    # game over, wins:
    # player 1: 1
    # player 2: 0
    #
    # ==================================================
    #
    # Word game:
    # round 1
    # player1: rock
    # player2: paper
    # player 2 won
    # game over, wins:
    # player 1: 0
    # player 2: 1
