import random


board = ['', '', '', '', '', '', '', '', '']


def draw_board():
    for index, box in enumerate(board):
        if index // 3 != (index - 1) // 3:
            print('—' * 13)
        if box:
            print('| ' + box + ' ', end='')
        else:
            print('|   ', end='')
        if index % 3 == 2:
            print('|')
        if index == 8:
            print('—' * 13)
            print()


def check_winner():
    if board[0] == board[1] == board[2] != '':
        return board[0]
    if board[3] == board[4] == board[5] != '':
        return board[3]
    if board[6] == board[7] == board[8] != '':
        return board[6]
    if board[0] == board[3] == board[6] != '':
        return board[0]
    if board[1] == board[4] == board[7] != '':
        return board[1]
    if board[2] == board[5] == board[8] != '':
        return board[2]
    if board[0] == board[4] == board[8] != '':
        return board[0]
    if board[2] == board[4] == board[6] != '':
        return board[2]


def check_tie():
    counter = 0
    for box in board:
        if box:
            counter += 1
    if counter == 9:
        return True
    return False


winner = ''
tie = False
while not winner or tie:
    draw_board()
    box_number = -1
    valid_input = False
    while not valid_input:
        box_number = int(input('Выбери номер клетки для хода крестиком 1-9:'))
        if box_number < 1 or box_number > 9:
            print('Выбери номер клетки для хода крестиком 1-9:')
        elif board[box_number - 1]:
            print('Эта клетка уже занята, выбери другой номер!')
        else:
            board[box_number - 1] = 'X'
            valid_input = True

    tie = check_tie()
    winner = check_winner()
    if winner:
        break
    if tie:
        break

    computer_play = -1
    while board[computer_play - 1] or computer_play == -1:
        computer_play = random.randint(1, 9)

    board[computer_play - 1] = 'O'

    winner = check_winner()
    if winner:
        break


if winner:
    if winner == 'X':
        print('')
        print('Отлично, ты победил, красавчик 🎉 🎆 🎉')
    else:
        print('')
        print('Победил искусственный интеллект 😒')
else:
    print('')
    print('На этот раз победила дружба 🤝 ')
draw_board()