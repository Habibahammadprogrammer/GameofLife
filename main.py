# libraries used
import numpy as np
import matplotlib.pyplot as plt

# creating initial board
board = np.random.randint(0, 3, size=(100, 100))
# array for storing age
age = [[0] * 100] * 100
# array for neighbours
neighbours = []
# global variables
NO_OF_FISH = 0
NO_OF_SHARKS = 0
GENERATION = 0


# get neighbours


def get_neighbours(i, j):
    global board
    global neighbours
    if i and j == 0:
        neighbours = [board[0][1], board[1][0], board[1][1]]
    elif i == 99 and j == 0:
        neighbours = [board[98][0], board[99][1], board[98][1]]
    elif i == 0 and j == 99:
        neighbours = [board[0][98], board[1][98], board[1][99]]
    elif i and j == 99:









        
        neighbours = [board[98][98], board[99][98], board[98][99]]
    elif [0 <= i <= 99 and (j == 0 or j == 99)] or [(i == 99 or i == 0) and 0 <= j <= 99]:
        neighbours = [board[i - 1][j], board[i - 1][j + 1], board[i + 1][j + 1], board[i + 1][j],
                      board[i + 1][j + 1]]

    else:
        neighbours = [board[i + 1][j - 1], board[i + 1][j + 1], board[i + 1][j], board[i][j - 1], board[i][j + 1],
                      board[i - 1][j - 1], board[i - 1][j], board[i - 1][j + 1]]

    return neighbours


# counting number of fish and number of sharks


def neighbour_analysis():
    global NO_OF_SHARKS, NO_OF_FISH
    for i in range(len(neighbours)):
        if neighbours[i] == 1:
            NO_OF_FISH += 1
        if neighbours[i] == 2:
            NO_OF_SHARKS += 1
    return NO_OF_FISH, NO_OF_SHARKS


# updating age for each cell


def update_age():
    for i in range(99):
        for j in range(99):
            if validate_age(i, j):
                age[i][j] += 1

    return age


# changing state of cell based on rules


def reset():
    global NO_OF_SHARKS, NO_OF_FISH, neighbours
    NO_OF_FISH = 0
    NO_OF_SHARKS = 0
    for i in range(len(neighbours)):
        neighbours[i] = 0


def display():
    global GENERATION, board
    plt.imshow(board, cmap='magma_r')
    plt.title(f"GENERATION {GENERATION}")
    plt.show()
    GENERATION = GENERATION + 1


def validate_age(i, j):
    if board[i][j] == 1:
        if age[i][j] == 10:
            age[i][j] = 0
            return False
        else:
            return True
    elif board[i][j] == 2:
        if age[i][j] == 20:
            age[i][j] = 0
            return False


def change_state(i, j):
    # empty cell
    if board[i][j] == 0:
        neighbour_analysis()
        if NO_OF_FISH > 4:
            board[i][j] = 1
            return board
        if validate_age(i, j):
            age[i][j] += 1
            return board
    elif NO_OF_SHARKS > 4:
        board[i][j] = 2
        if validate_age(i, j):
            age[i][j] += 1
            return board
        # fish rules
    elif board[i][j] == 1:
        if not validate_age(i, j):
            board[i][j] = 0
            return board
        else:
            neighbour_analysis()
        if NO_OF_FISH == 8 or NO_OF_SHARKS >= 5:
            board[i][j] = 0
            age[i][j] = 0
            return board
        # shark rules
    else:
        if NO_OF_SHARKS >= 6 and NO_OF_FISH == 0:
            board[i][j] = 0
            age[i][j] = 0
            return board


def main():
    global GENERATION
    for gen in range(999):
        display()
        reset()
        for i in range(99):
            for j in range(99):
                get_neighbours(i, j)
                neighbour_analysis()
                change_state(i, j)
                update_age()


if __name__ == "__main__":
    main()
