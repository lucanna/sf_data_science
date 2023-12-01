"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов компьютер угадывает число

    Args:
        random_predict (_type_): функция угадывания_

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем начальные условия для воспроизводимости кода
    random_array = np.random.randint(1, 101, size=(1000)) # загадываем числа, составляем из них список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Компьютер угадывает число в среднем за: {score} попыток')
    return(score)

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    min_ = 0
    max_ = 101    
    mid = (min_ + max_) // 2
    
    while number != mid:
        count +=1
        if number > mid:
            min_ = mid    
        else:
            max_ = mid
        mid = (min_ + max_) // 2
    return count

if __name__ == '__main__':
    score_game(random_predict)