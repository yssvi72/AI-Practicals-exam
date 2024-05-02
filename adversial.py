import math

EMPTY, PLAYER_X, PLAYER_O = 0, 1, -1

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY: return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY: return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY: return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY: return board[0][2]
    return 0

def game_over(board): return evaluate(board) != 0 or all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def possible_moves(board): return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def make_move(board, move, player):
    i, j = move
    new_board = [row[:] for row in board]
    new_board[i][j] = player
    return new_board

def minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board): return evaluate(board)
    return max(minimax(make_move(board, move, PLAYER_X), depth - 1, False) for move in possible_moves(board)) if maximizing_player else min(minimax(make_move(board, move, PLAYER_O), depth - 1, True) for move in possible_moves(board))

def find_best_move(board):
    best_move, max_eval = None, -math.inf
    for move in possible_moves(board):
        eval = minimax(make_move(board, move, PLAYER_X), 8, False)
        if eval > max_eval:
            max_eval, best_move = eval, move
    return best_move

def display_board(board):
    for row in board: print(' | '.join('X' if x == PLAYER_X else 'O' if x == PLAYER_O else ' ' for x in row))
    print('-' * 9)

board = [[EMPTY] * 3 for _ in range(3)]
print("Welcome to Tic-Tac-Toe!\n\nThe positions are represented as follows:\n 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n\nPlayer plays with 'O', AI plays with 'X'\n")
display_board(board)

while not game_over(board):
    print("\nPlayer's Turn:")
    move = int(input("Enter your move (1-9): ")) - 1
    x, y = move // 3, move % 3
    if board[x][y] != EMPTY:
        print("Invalid move, try again.")
        continue
    board[x][y] = PLAYER_O
    display_board(board)
    if game_over(board): break
    print("\nAI's Choices:")
    for i, move in enumerate(possible_moves(board), start=1):
        new_board = make_move(board, move, PLAYER_X)
        eval_score = minimax(new_board, 8, False)
        print(f"{i}. Row: {move[0] + 1}, Column: {move[1] + 1} - Evaluation Score: {eval_score}")
    print("\nAI's Turn:")
    ai_move = find_best_move(board)
    print(f"AI chooses to place 'X' at row {ai_move[0] + 1}, column {ai_move[1] + 1}")
    board[ai_move[0]][ai_move[1]] = PLAYER_X
    display_board(board)
    print("==============================")

winner = evaluate(board)
if winner == PLAYER_X: print("\nAI wins!")
elif winner == PLAYER_O: print("\nPlayer wins!")
else: print("\nIt's a draw!")
