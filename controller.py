
class Controller:
    def __init__(self, funcs_1, funcs_2, names=None):
        self.names = names
        self.legacy = [len(x) == 2 for x in (funcs_1, funcs_2)]
        self.strategy = funcs_1[0], funcs_2[0]
        self.turn = funcs_1[1] if self.legacy[0] else None, \
                    funcs_2[1] if self.legacy[1] else None

        self.game_logs = [[], []]
        self.points = [0, 0]

    def new_game(self, debug=False):
        choices = [self.strategy[i](self.game_logs[i]) for i in range(2)]

        if debug:
            print("Start round.")

        # Hack together legacy support
        for i in range(2):
            if not self.legacy[i]:
                continue

            for j in range(1, 100):
                if self.turn[i](j, *choices[i]) == False:
                    choices[i] = j
                    break
            if type(choices[i]) is not int:
                choices[i] = 100

        # Check for acceptable values
        for i in range(2):
            try:
                choices[i] = int(choices[i])
            except ValueError:
                name = f"Player {i + 1}" if self.names is None else self.names[i]
                raise Exception(f"{name} gives non-numeric value {choices[i]}")

            if not 1 <= choices[i] <= 100:
                name = f"Player {i + 1}" if self.names is None else self.names[i]
                raise Exception(f"{name} gives unacceptable value {choices[i]}")

        # Work out who's won
        if choices[0] == choices[1] == 100:
            if debug:
                print(f"Players have mutually reached 100, and are awarded 100 points each.")
            self.points[0] += 100
            self.points[1] += 100

            for x in self.game_logs:
                x.append((100, True))
        elif choices[0] == choices[1]:
            if debug:
                print(f"Both players stop counting at {choices[0]}. No points.")
            for x in self.game_logs:
                x.append((choices[0], False))
        else:
            winner = 1 if choices[0] > choices[1] else 0
            loser = 0 if winner == 1 else 1
            value = choices[winner]
            self.points[winner] += value * 2
            
            self.game_logs[winner].append((value, True))
            self.game_logs[loser].append((value, False))

            if debug:
                print(f"{value}: player {winner + 1} stops counting, player {loser + 1} keeps counting. Player {winner + 1} gets {value * 2} points.")

    def run(self, number_of_games, debug=False):
        no_debug = 0
        for _ in range(number_of_games):
            if debug:
                if no_debug == 0:
                    self.new_game(debug=True)
                else:
                    self.new_game(debug=False)
                    no_debug -= 1
            else:
                self.new_game(debug=False)

            if debug and no_debug == 0:
                print(f"\nCurrent points: {self.points}")
                count = input("Start next game with [ENTER], or skip debug output by typing how many games to skip for: ").strip()
                if count == "":
                    continue
                no_debug = int(count)

        if debug:
            print(f"Ends with points: {self.points}")

        return self.points
