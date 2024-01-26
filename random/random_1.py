"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
from time import *
start = time()
end = time()

def chess_work():
    while start - end <1800:

        step = input('Куда сходите? ')
        if step == 'off':
            break

        cost = time() - start #затраты времени
        have_time = time() #осталось времени
        print('Вы потратили на ход:', round(cost), 'с')
        cost_all = (start - time() + 1800) / 60
        print('Всего осталось:', round(cost_all), 'мин.')
chess_work()
