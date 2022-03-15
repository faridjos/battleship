from random import randint
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("battleship")


class Ships:
    """
    Store positions of ships and enemy guesses
    """
    grid_size = 5
    number_of_ships = 4

    def __init__(self):
        self.coordinates = []
        self.guesses = []
        self.score = 0

    def rand_coord(self):
        """generates random position
        """
        x = randint(0, Ships.grid_size - 1)
        y = randint(0, Ships.grid_size - 1)

        return (x, y)

    def add_xy_to_list(self, fun, array):
        """
        Add coordinates to a list with no duplicates
        """
        while True:
            (x, y) = fun()
            if (x, y) not in array:
                array.append((x, y))
                break

    def position_ships(self):
        """
        Generate random positions for ships
        """
        for _ in range(Ships.number_of_ships):
            self.add_xy_to_list(self.rand_coord, self.coordinates)

    def hit(self):
        """Checks if enemy hit a ship"
        """
        for (x, y) in self.coordinates:
            hit = self.guesses[-1] == (x, y)
            if hit:
                self.score += 1
                return True
        return hit


class Human:
    """
    Has method to input name and check if not empty string
    """
    def __init__(self):
        """
        User inputs name
        """
        while True:
            name = input("Enter your name:\n")
            if name != '':
                break
        self.name = name


class HumanPlayer(Ships, Human):
    """Has method to guess enemy ship coordinates and print grid
    """
    def __init__(self):
        Human.__init__(self)
        Ships.__init__(self)
        self.my_guesses = []

    def input_coord(self):
        """User enters ship coordinates which are then validated
        """
        while True:
            x = input("Guess x-coordinate:\n")
            if x.isdigit():
                x = int(x)
                if 0 <= x < self.grid_size:
                    break
                else:
                    print(f"x and y must be 0- {self.grid_size - 1}")
            else:
                print("You must enter an integer!")

        while True:
            y = input("Guess y-coordinate:\n")
            if y.isdigit():
                y = int(y)
                if 0 <= y < self.grid_size:
                    break
                else:
                    print(f"x and y must be 0- {self.grid_size - 1}")
            else:
                print("You must enter an integer!")

        return (x, y)

    def guess_coordinates(self):
        """User enters enemy ship coordinates to try to hit
        """
        while True:
            (x, y) = self.input_coord()
            if (x, y) not in self.my_guesses:
                self.my_guesses.append((x, y))
                break
            else:
                print(f"You already guessed position {(x, y)}, try again")

    def print_grid(self):
        """
        Print grid. Ships are shown as "@" and shots as "X"
        """
        for i in range(Ships.grid_size):
            for j in range(Ships.grid_size):
                shot = False
                for (x, y) in self.guesses:
                    shot = (i, j) == (x, y)
                    if shot:
                        print('X ', end=' ')
                        break
                if not shot:
                    found_ship = False
                    for (x, y) in self.coordinates:
                        found_ship = (i, j) == (x, y)
                        if found_ship:
                            print('@ ', end=' ')
                            break
                    if not found_ship:
                        print('. ', end=' ')
            print('')


class ComputerPlayer(Ships):
    """Has method to guess enemy ship coordinates and print grid
    """
    def __init__(self):
        Ships.__init__(self)
        self.my_guesses = []

    def guess_coordinates(self):
        """Computer generates random enemy ship coordinates to try to hit
        """
        self.add_xy_to_list(self.rand_coord, self.my_guesses)

    def print_grid(self):
        """
        Print grid. Ships are not shown, shots are shown as 'X'
        """
        for i in range(Ships.grid_size):
            for j in range(Ships.grid_size):
                shot = False
                for (x, y) in self.guesses:
                    shot = (i, j) == (x, y)
                    if shot:
                        print('X ', end=' ')
                        break
                if not shot:
                    print('. ', end=' ')
            print('')


def store_score(score):
    """
    Store scores in google sheet
    """
    print("Sending score to google sheet...")
    score_sheet = SHEET.worksheet('score_sheet')
    score_sheet.append_row(score)
    print('Storing score in score_sheet successful.\n')


def get_last_5_scores():
    """
    Collect the last 5 scores
    """
    score_sheet = SHEET.worksheet('score_sheet')
    data = score_sheet.get_all_values()
    nr_of_rows = len(data)
    ind_max = min(nr_of_rows, 5)

    rows = []
    for ind in range(-ind_max, 0):
        row = data[ind]
        rows.append(row)

    return rows

def print_game_info():
    """Show information about the game
    """
    print("Welcome to the Battleship game!\n")


def main():
    """Main program
    """
    while True:
        print_game_info()

        player = HumanPlayer()
        print("")
        player.position_ships()
        player.print_grid()
        print("")

        computer = ComputerPlayer()
        computer.position_ships()
        computer.print_grid()
        print('')

        while True:
            computer.guess_coordinates()
            player.guesses = computer.my_guesses
            print(f"Computer guessed {player.guesses[-1]}")
            if player.hit():
                print("Computer hit")
            else:
                print("Computer missed")
            print('')

            player.guess_coordinates()
            computer.guesses = player.my_guesses
            print(f"{player.name} guessed {computer.guesses[-1]}")
            if computer.hit():
                print(f"{player.name} hit")
            else:
                print(f"{player.name} missed")
            print('')

            print(f"Score: {player.name} {computer.score}",  end=" ")
            print(f"Computer {player.score}")
            print('')

            player.print_grid()
            print('')
            computer.print_grid()
            print('')
            n = Ships.number_of_ships
            if n in (player.score, computer.score):
                if player.score != computer.score:
                    winner = player.name if computer.score == n else "Computer"
                    print(f"The winner is {winner}")
                else:
                    winner = f"{player.name} and Computer"
                    print(f"The winners are {winner}")
                print('')
                score = [computer.score, player.score]
                store_score(score)
                print("The previous scores are: ")
                print(get_last_5_scores())
                print(" ")

            string = input("Enter any key to continue or no to stop\n")
            print('')
            if string.lower() == 'no':
                break

        string = input("Enter any key to start a new game or no to stop\n")
        print('')
        if string.lower() == 'no':
            break
        


main()
