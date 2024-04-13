import os

y = "🟡"
r = "🔴"
b = "⬛"

grid = [
   # 1  2  3  4  5  6  7
    [b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b],
]


def print_grid():
    print(f"  1   2    3   4   5    6   7")
    print(f"+-----------------------------+")
    print(f"|{grid[0][0]}|{grid[0][1]}|{grid[0][2]}|{grid[0][3]}|{grid[0][4]}|{grid[0][5]}|{grid[0][6]}|")
    print(f"|-----------------------------|")
    print(f"|{grid[1][0]}|{grid[1][1]}|{grid[1][2]}|{grid[1][3]}|{grid[1][4]}|{grid[1][5]}|{grid[1][6]}|")
    print(f"|-----------------------------|")
    print(f"|{grid[2][0]}|{grid[2][1]}|{grid[2][2]}|{grid[2][3]}|{grid[2][4]}|{grid[2][5]}|{grid[2][6]}|")
    print(f"|-----------------------------|")
    print(f"|{grid[3][0]}|{grid[3][1]}|{grid[3][2]}|{grid[3][3]}|{grid[3][4]}|{grid[3][5]}|{grid[3][6]}|")
    print(f"|-----------------------------|")
    print(f"|{grid[4][0]}|{grid[4][1]}|{grid[4][2]}|{grid[4][3]}|{grid[4][4]}|{grid[4][5]}|{grid[4][6]}|")
    print(f"|-----------------------------|")
    print(f"|{grid[5][0]}|{grid[5][1]}|{grid[5][2]}|{grid[5][3]}|{grid[5][4]}|{grid[5][5]}|{grid[5][6]}|")
    print(f"+-----------------------------+")


whose_move_is_it = y

# THE MAIN BIT
if __name__ == '__main__':
    while True:
        read_a_number = False
        while read_a_number == False:
            try:
                move_number = int(input(f"It is {whose_move_is_it} move. Please enter a number 1-7:"))
                if move_number < 1 or move_number > 7:
                    print("That's not a number 1-7, you wally!")
                else:
                    read_a_number = True
            except ValueError:
                print("That's not a number 1-7, you nincompoop!")

        print(f"{whose_move_is_it} entered move {move_number}")

        # change grid to have whose_move_is_it's circle in the
        # right row in column number move_number (1-7)

        move_made_successfully = True

        if grid[5][move_number - 1] == b:
            grid[5][move_number - 1] = whose_move_is_it
        elif grid[4][move_number - 1] == b:
            grid[4][move_number - 1] = whose_move_is_it
        elif grid[3][move_number - 1] == b:
            grid[3][move_number - 1] = whose_move_is_it
        elif grid[2][move_number - 1] == b:
            grid[2][move_number - 1] = whose_move_is_it
        elif grid[1][move_number - 1] == b:
            grid[1][move_number - 1] = whose_move_is_it
        elif grid[0][move_number - 1] == b:
            grid[0][move_number - 1] = whose_move_is_it
        else:
            print(f"Column {move_number} is full, you {whose_move_is_it} poo head!")
            move_made_successfully = False

        if move_made_successfully:

            print_grid()

            # see if the player who made the move won

            # if no one has won yet, switch sides
            if whose_move_is_it == y:
                whose_move_is_it = r
            elif whose_move_is_it == r:
                whose_move_is_it = y
