from typing import List, Union


def median(values: List[Union[int, float]]) -> Union[int, float]:
    """Фунция для вычисления медианы
    :param list values: Список целых чисел или чисел с плавующей запятой
    :return: Число, являющееся медианой
    """
    sorted_values = sorted(values)
    values_length = len(sorted_values)
    if values_length % 2 != 0:
        return sorted_values[values_length // 2]
    else:
        return (sorted_values[values_length // 2] + sorted_values[values_length // 2 - 1]) / 2
