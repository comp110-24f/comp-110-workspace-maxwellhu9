""""""

__author__ = "730759980"


def all(a_list: list[int], num1: int) -> bool:
    if len(a_list) == 0:
        return False

    i = 0

    while i < len(a_list):
        if a_list[i] != num1:
            return False
        i += 1

    return True


def max(a_list: list[int]) -> int:
    if len(a_list) == 0:
        raise ValueError("max() arg is an empty List")

    largest = a_list[0]
    i = 1
    while i < len(a_list):
        if a_list[i] > largest:
            largest = a_list[i]
        i += 1

    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False

    i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    i = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1
