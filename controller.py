
class Controller:
    def __init__(self, funcs_1, funcs_2):
        self.strategy = funcs_1[0], funcs_2[0]
        self.turn = funcs_1[1], funcs_2[1]

        self.game_logs = [[], []]
        self.points = [0, 0]

    def new_game(self, debug=False):
        self.current_value = 1

        args = [self.strategy[i](self.game_logs[i]) for i in range(2)]

        if debug:
            print("Start game.")

        for _ in range(99):
            choices = [self.turn[i](self.current_value, *args[i]) for i in range(2)]

            if choices[0] and choices[1]:
                if debug:
                    print(f"{self.current_value}: both players keep counting.")
                self.current_value += 1
            elif not choices[0] and not choices[1]:
                if debug:
                    print(f"{self.current_value}: both players stop counting. No points.")
                for x in self.game_logs:
                    x.append((self.current_value, False))
                break
            else:
                winner = 1 if choices[0] else 0
                loser = 0 if choices[0] else 1
                self.points[winner] += self.current_value * 2
                
                self.game_logs[winner].append((self.current_value, True))
                self.game_logs[loser].append((self.current_value, False))

                if debug:
                    print(f"{self.current_value}: player {winner + 1} stops counting, player {loser + 1} keeps counting. Player {winner + 1} gets {self.current_value * 2} points.")
                break
            
        if self.current_value == 100:
            if debug:
                print(f"Players have mutually reached 100, and are awarded 100 points each.")
            self.points[0] += 100
            self.points[1] += 100

            for x in self.game_logs:
                x.append((self.current_value, True))

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
