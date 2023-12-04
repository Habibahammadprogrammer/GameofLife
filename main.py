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
    if (i and j == 0) or (i == 0 and j == 99) or (i == 99 and j == 0) or (i == 99 and j == 99):
        neighbours = [board[i - 1][j], board[i - 1][j + 1], board[i + 1][j + 1], board[i + 1][j], board[i + 1][j + 1]]
        return neighbours
    else:
        neighbours = [board[i + 1][j - 1], board[i + 1][j + 1], board[i + 1][j], board[i][j - 1], board[i][j + 1],
                      board[i - 1][j - 1], board[i - 1][j], board[i - 1][j + 1]]
    return neighbours


# counting number of fish and number of sharks


def neighbour_analysis(i, j):
    global NO_OF_SHARKS, NO_OF_FISH
    for index in range(len(neighbours)):
        if neighbours[i][j] == 1:
            NO_OF_FISH += 1
        if neighbours[i][j] == 2:
            NO_OF_SHARKS += 1


# updating age for each cell


def update_age():
    for i in range(99):
        for j in range(99):
            if board[i][j] == 0:
                age[i][j] += 1
    return age


# changing state of cell based on rules


def change_state(i, j):
    if board[i][j] == 0:
        neighbour_analysis(i, j)
    if NO_OF_FISH > 4:
        board[i][j] == 1
        age[i][j] += 1
    elif NO_OF_SHARKS > 4:
        board[i][j] == 2
        age[i][j] += 1
        # Second and third rule
    elif board[i][j] == 1:
        if age[i][j] == 10:
            board[i][j] = 0
            age[i][j] = 0
        else:
            neighbour_analysis(i, j)
        if (NO_OF_FISH == 8 or NO_OF_SHARKS >= 5):
            board[i][j] = 0
            age[i][j] += 1




def display(board):
    global GENERATION
    plt.imshow(board, cmap='magma_r')
    plt.title(f"GENERATION {GENERATION}")
    plt.show()
    GENERATION = GENERATION + 1
def main():
 global GENERATION
 for gen in range(999):
    for i in range(99):
        for j in range(99):
            get_neighbours(i, j)
            neighbour_analysis(i, j)
            change_state(i, j)
            update_age()
    display(board)
if __name__ == "__main__":
    main()
