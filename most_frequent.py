import sys
from typing import List, Set, Tuple

sys.setrecursionlimit(1000)


def most_frequent(receipts: List[List[str]]) -> Tuple[List[Set[str]], int]:
    """Функция для нахождения самых частых сочетаний товаров чеке
    :param list receipts: Список чеков с наименованиями
    :return: list
        Список с самыми частыми сочетаниями
    :return: int
        Число, показывающее максимальное число повторов
    """
    receipts_set = []
    for receipt in receipts:
        receipts_set.append(set(receipt))
    max_counter_value = 2
    most_frequent = []
    for i in range(len(receipts_set)):
        current_max_counter_value = 0
        current_most_frequent, current_max_counter_value = most_frequent_rec(receipts_set[i],
                                                                             receipts_set,
                                                                             current_max_counter_value)
        if current_max_counter_value > max_counter_value:
            max_counter_value = current_max_counter_value
            most_frequent = [current_most_frequent]
        elif current_max_counter_value == max_counter_value and current_most_frequent not in most_frequent:
            most_frequent.append(current_most_frequent)
    return most_frequent, max_counter_value


def most_frequent_rec(current: Set[str], rest: List[Set[str]], current_max_counter_value: int) -> Tuple[Set[str], int]:
    """Рекурсивна функция для поиска для самого частого сочетания для определенного чека
    :param current: set
        Текущее сочетание
    :param list rest: Оставшиеся чеки
    :param current_max_counter_value: int
        Число повторов для текущего сочетания
    :return set: Найденное сочетание
    :return int: Число повторов, найденного сочетания
    """
    if not rest:
        return current, current_max_counter_value
    current_most_frequent = current & rest[0]
    if len(current_most_frequent) > 1:
        current_max_counter_value += 1
        current = current_most_frequent
    rest = rest[1:]
    current, current_max_counter_value = most_frequent_rec(current, rest, current_max_counter_value)
    return current, current_max_counter_value
