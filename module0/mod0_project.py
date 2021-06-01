import numpy as np


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v3(number):
    """Используем метод бинарного деления - выбираем число посередине от 1 до 100,
    проверяем находится ли оно в отрезке 1-50 или 51-100 и потом такимже образом делим соответствующий отрезок.
    Получаем алгоритм способный находить решение за log(n) попыток"""
    count = 1
    predict = 50
    up_bound = 101
    low_bound = 1
    while number != predict:
        count += 1
        if number > predict:
            low_bound = predict
            predict = (up_bound + low_bound) // 2
        else:
            up_bound = predict
            predict = (up_bound + low_bound) // 2
    return count
