from decimal import Decimal
from typing import List, Dict, Union


def calculate_expected_value(values: List[Union[int, float]]) -> Decimal:
    """Функция для вычисления матожидания
    :param list values: Список целых чисел или чисел с плавующей запятой
    :return float: Матожидание
    """
    expected_value = 0
    num_probabilities = calculate_num_probabilities(values)
    for key in num_probabilities.keys():
        expected_value += Decimal(key) * num_probabilities[key]
    expected_value = Decimal(expected_value).quantize(Decimal('.0001'))
    return expected_value


def calculate_num_probabilities(values: List[Union[int, float]]) -> Dict[Union[int, float], Decimal]:
    """Функция для подсчета вероятностей чисел в списке
    :param list values: Список целых чисел или чисел с плавующей запятой
    :return dict: Словарь формата число - вероятность
    """
    num_probabilities = {}
    for value in values:
        if value not in num_probabilities:
            num_probabilities[value] = 1
        else:
            num_probabilities[value] += 1
    for key in num_probabilities:
        num_probabilities[key] = Decimal(num_probabilities[key] / len(values)).quantize(Decimal('.0001'))
    return num_probabilities
