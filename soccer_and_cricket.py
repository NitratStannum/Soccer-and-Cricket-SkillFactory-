'''Игра "Крестики - нолики"

Итоговое практическое задание курса "Введение в Python", модуль B5

'''

import random

# Создадим игровое поле:
game_zone = [[' '] * 3 for i in range(3)]

# Создадим переменные, в которые будет сохраняться прогресс игры

game_log = [] # сюда записываются координаты ходов
error_log = [] # сюда записываются ходы, которые нельзя совершить (например если клетка уже занята)
move_number = 0 # счетчик ходов

# Создадим необходимые для игры функции

def show_game_zone():
    """" Функция выводит игровое поле в консоль"""

    print(f' |  0  |  1  |  2  |')
    print(' -------------------')
    print(f'0|  {game_zone[0][0]}  |  {game_zone[0][1]}  |  {game_zone[0][2]}  |')
    print(' -------------------')
    print(f'1|  {game_zone[1][0]}  |  {game_zone[1][1]}  |  {game_zone[1][2]}  |')
    print(' -------------------')
    print(f'2|  {game_zone[2][0]}  |  {game_zone[2][1]}  |  {game_zone[2][2]}  |')
    print(' -------------------')


def welcome_screen(): 
    """ Функция для вывода приветственной информации"""
    
    print('_' * 20)
    print(' Приветствуем Вас')
    print('      в игре     ')
    print('"Крестики - Нолики"')
    print('_' * 20)
    print('\nИгровое поле выглядит следующим образом:')
    print('')
    show_game_zone()
    print('')
    print('Прежде чем начать, выберите режим игры')
    print('')

def players_move_X():
    """Функция для ввода координат хода игрока (игрок ходит крестиком)"""

    print('Куда хотите поставить крестик ?')
    while True:
        while True:
            move_x = int(input('Введите координату по горизонтали (от 0 до 2): '))
            if 0 > move_x or move_x > 2:
                print("Ваше значение вне диапазона. Введите значение от 0 до 2.")
                continue
            else:
                break

        while True:
            move_y = int(input('Введите координату по вертикали (от 0 до 2): '))
            if 0 > move_y or move_y > 2:
                print("Ваше значение вне диапазона. Введите значение от 0 до 2.")
                continue
            else:
                break

        if [move_x, move_y] in game_log:
            print("Клетка уже занята")
            continue
        else:
            game_zone[move_y][move_x] = 'X'
            game_log.append([move_x, move_y])
            break

def players_move_0():
    """Функция для ввода координат хода игрока (игрок ходит ноликом)"""

    print('Куда хотите поставить нолик ?')
    while True:
        while True:
            move_x = int(input('Введите координату по горизонтали (от 0 до 2): '))
            if 0 > move_x or move_x > 2:
                print("Ваше значение вне диапазона. Введите значение от 0 до 2.")
                continue
            else:
                break

        while True:
            move_y = int(input('Введите координату по вертикали (от 0 до 2): '))
            if 0 > move_y or move_y > 2:
                print("Ваше значение вне диапазона. Введите значение от 0 до 2.")
                continue
            else:
                break

        if [move_x, move_y] in game_log:
            print("Клетка уже занята")
            continue
        else:
            game_zone[move_y][move_x] = '0'
            game_log.append([move_x, move_y])
            break

def comp_move():
    """Функция для совершения хода компьютером (компьютер ходит ноликом)"""

    while True:
        x_zone = random.randint(0,2)
        y_zone = random.randint(0,2)
        comp_move_log = [x_zone, y_zone]
        if comp_move_log not in game_log:
            game_zone[y_zone][x_zone] = "0"
            game_log.append([x_zone, y_zone])
            break
        else:
            error_log.append({'Ошибка: поле занято': [x_zone, y_zone]})
            continue

def check_win():
    win_combs_tuple = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                      ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                      ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for comb in win_combs_tuple:
        zone_list = []
        for coord in comb:
            zone_list.append(game_zone[coord[0]][coord[1]])
            if zone_list == ["X", "X", "X"]:
                win_text = 'Выиграл Х'
                print('\n', win_text)
                return True
            if zone_list == ["0", "0", "0"]:
                win_text = 'Выиграл 0'
                print('\n', win_text)
                return True
            if len(game_log) == 9:
                win_text = 'Ничья. Победила дружба =)'
                print('\n', win_text)
                return True
    return False

def game_mode():
    game_mode_inp = int(input('Если хотите играть против компьютера, введите 1.\n'
                      'Если хотите играть против другого игрока, введите 2: '))
    return game_mode_inp


# Пропишем игровой цикл:

welcome_screen()

# game_mode = int(input('Если хотите играть против компьютера, введите 1.\n'
#                       'Если хотите играть против другого игрока, введите 2: '))

if game_mode() == 2:
    
    print('\n Выбран режим "Игрок против игрока". Первым ходит крестик.')
    while True:
        players_move_X()
        show_game_zone()
        move_number += 1

        if check_win():
            break

        players_move_0()
        show_game_zone()
        move_number += 1

        if check_win():
            break

        
elif game_mode() == 1:
    print('\n Выбран режим "Игрок против компьютера". Вы ходите крестиком')
    while True:
        players_move_X()
        move_number += 1

        if check_win():
            show_game_zone()
            break

        comp_move()
        show_game_zone()
        move_number += 1

        if check_win():
            break

        












    

    

    











    

    

       
















