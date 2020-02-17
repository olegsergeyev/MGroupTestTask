from typing import List, Union


def calculate_moda(values: List[Union[int, float]]) -> List[Union[int, float]]:
    """Функция для вычисления моды списка
    :param list values: Список целых чисел или чисел с плавующей запятой
    :return list: Список всех чисел, являющихся модой
    """
    moda = []
    num_count = {}
    for value in values:
        if value not in num_count:
            num_count[value] = 1
        else:
            num_count[value] += 1
    max_counter_value = max(num_count.values())
    for key, value in num_count.items():
        if value == max_counter_value:
            moda.append(key)
    return moda
