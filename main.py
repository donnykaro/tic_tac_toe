import sys

board_dict = {7: ' ', 8: ' ', 9: ' ', 4: ' ', 5: ' ', 6: ' ', 1: ' ', 2: ' ', 3: ' '}


def restart():
    global board_dict
    if (player_names[0][1] or player_names[1][1]) > 0:
        board_dict = board_dict.fromkeys(board_dict, ' ')


def win(player_name: str):
    print(f"Brawo, {player_name} wygral/la")
    return True


def check_if_win(player_name: str):
    # checks for empty cell in 1, 2, 3 in a row, then == them for same value, like 'X' or 'O'
    for i in range(1, 8, 3):
        if board_dict[i] != ' ' and board_dict[i+1] != ' ' and board_dict[i+2] != ' ' \
                and board_dict[i] == board_dict[i+1] == board_dict[i+2]:
            return win(player_name)

    for i in range(1, 4):
        if board_dict[i] != ' ' and board_dict[i + 3] != ' ' and board_dict[i + 6] != ' ' \
                and board_dict[i] == board_dict[i + 3] == board_dict[i + 6]:
            return win(player_name)

    if board_dict[1] != ' ' and board_dict[5] != ' ' and board_dict[9] != ' ' and board_dict[1] == board_dict[5] == \
            board_dict[9]:
        return win(player_name)
    elif board_dict[3] != ' ' and board_dict[5] != ' ' and board_dict[7] != ' ' and board_dict[3] == board_dict[5] == \
            board_dict[7]:
        return win(player_name)
    else:
        return False


def check_if_draw():
    if ' ' not in board_dict.values():
        print("Remis")
        return True


def check_if_play_again():
    start_again = input("Chcesz zagrac jeszcze raz? tak albo nie: ")
    if start_again.isalpha() and 'T' in start_again.upper():
        start_game(player_names)
    elif start_again.isalpha() and 'N' in start_again.upper():
        print("Dzieki za gre!")
        sys.exit(0)
    elif (start_again.isalpha() and ('N' or 'T' not in start_again.upper())) or not start_again.isalpha():
        print('Tak ciezko podazac za instrukcja?')
        sys.exit(0)


def check_if_win_or_draw(player_name: str):
    if check_if_win(player_name) or check_if_draw():
        if player_names[0][0] == player_name:
            player_names[0][1] += 1
        else:
            player_names[1][1] += 1
        print(f"{player_names[0][0]} ma {player_names[0][1]} wygranych gier")
        print(f"{player_names[1][0]} ma {player_names[1][1]} wygranych gier")

        check_if_play_again()

    return True


def update_board_dict(index: int, value: str, player_name: str):
    if board_dict[index] == ' ':
        board_dict[index] = value
        display_board()

        if check_if_win_or_draw(player_name) is not None:
            return True

    else:
        display_board()
        print('Pole zajete, wybierz inne')
        return False


def display_board():
    column_count = 0
    current_row = []
    print('---------')
    for i in board_dict:
        current_row.append(board_dict[i])
        column_count += 1
        if column_count == 3 and len(current_row) == 3:
            print(f'{current_row[0]} | {current_row[1]} | {current_row[2]}')
            current_row = []
            column_count = 0
            print('---------')


def check_pos_update_board(player_name, player_x_or_o):
    try:
        position = int(input(f"{player_name}, wybierz pozycje 1-9: "))
    except ValueError:
        print("Podaj liczbe staloprzecinkowa")
        return False
    else:
        if not 0 < position < 10:
            print("pozycia musi byc pomiedzy 1 a 9")
            return False
        else:
            if update_board_dict(position, player_x_or_o, player_name) is False:
                return False
            else:
                return True


def start_game(player_names):
    restart()
    display_board()
    while True:
        player_uno = input("Chcesz grac jako X czy O?")
        if player_uno.isalpha() and player_uno.upper() == 'X':
            # why does this work?!
            player_uno_value = 'X'
            player_dos_value = 'O'
            print(f"{player_names[0][0]} zaczyna jako X")
            print(f"{player_names[1][0]} zaczyna jako O")
        elif player_uno.isalpha() and player_uno.upper() == 'O':
            player_uno_value = 'O'
            player_dos_value = 'X'
            print(f"{player_names[0][0]} zaczyna jako O")
            print(f"{player_names[1][0]} zaczyna jako X")
        else:
            continue

        while True:
            for i in range(1, 3):
                while True:
                    if i == 1:
                        if check_pos_update_board(player_names[0][0], player_uno_value):
                            break
                        else:
                            continue
                    else:
                        if check_pos_update_board(player_names[1][0], player_dos_value):
                            break
                        else:
                            continue


player_names = []
for s in range(0, 2):
    player_names.append([input("Podaj imie pierwszego gracza: "), 0])
start_game(player_names)
