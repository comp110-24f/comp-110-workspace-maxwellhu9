def get_first(list1: list[str]) -> str:
    return list1[0]


def remove_first(list1: list[str]) -> None:
    list1.pop(0)


def get_and_remove_first(list1: list[str]):
    x = get_first(list1)
    remove_first(list1)
    return x


list1 = ["1", "2", "3"]

print(get_and_remove_first(list1))
print(list1)
