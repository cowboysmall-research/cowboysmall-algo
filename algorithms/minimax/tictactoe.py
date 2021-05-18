import sys
import math
import random
import requests



def row_string(row):
    return '  {} | {} | {}  \n'.format(row[0], row[1], row[2])

def board_string(board):
    return '{}\n'.format(' ---+---+--- \n'.join([row_string(board[(i * 3):(i * 3) + 3]) for i in range(3)]))




def legal_moves(board):
    return [i for i in range(len(board)) if board[i] == '.']

def move(board, position, player):
    return [player if i == position else board[i] for i in range(len(board))]




def next_player(player):
    return 'X' if player == 'O' else 'O'




def has_row(board, player):
    return any(board[(i * 3):(i * 3) + 3].count(player) == 3 for i in range(3))

def has_column(board, player):
    return any([board[i], board[i + 3], board[i + 6]].count(player) == 3 for i in range(3))

def has_diagonal(board, player):
    return [board[0], board[4], board[8]].count(player) == 3 or [board[2], board[4], board[6]].count(player) == 3




def board_win(board, player):
    return has_row(board, player) or has_column(board, player) or has_diagonal(board, player)

def board_full(board):
    return len([p for p in board if p == '.']) == 0

def game_over(board):
    return board_win(board, 'X') or board_win(board, 'O') or board_full(board)




def player_win(board):
    return 'X' if board_win(board, 'X') else 'O' if board_win(board, 'O') else None




def get_move(board, player):
    if player == 'X':
        return int(input('X to move: ')) - 1
    else:
        print('O to move:')
        return best_move(board, player)




def best_move(board, player):
    best_score     = -math.inf
    best_position  = None

    for position in legal_moves(board):

        score = minimax(move(board, position, player), next_player(player), -math.inf, math.inf)

        if score > best_score:
            best_score     = score
            best_position  = position

    return best_position




def minimax(board, player, alpha, beta):
    if game_over(board):
        return ['X', None, 'O'].index(player_win(board)) - 1

    best_score = -math.inf if player == 'O' else math.inf

    for position in legal_moves(board):

        score = minimax(move(board, position, player), next_player(player), alpha, beta)

        if player == 'O':
            best_score = max(best_score, score)
            alpha      = max(best_score, alpha)
        else:
            best_score = min(best_score, score)
            beta       = min(best_score, beta)

        if beta <= alpha:
            return best_score

    return best_score




def main(argv):
    print('\nTic Tac Toe Simulator\n')
    print('\n{}\n'.format(board_string(range(1, 10))))

    board  = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    player = 'X'

    while not game_over(board):
        board  = move(board, get_move(board, player), player)
        player = next_player(player)

        print('\n{}\n'.format(board_string(board)))

    print('X wins\n' if board_win(board, 'X') else 'O wins\n' if board_win(board, 'O') else 'Draw\n')




if __name__ == "__main__":
    main(sys.argv[1:])
