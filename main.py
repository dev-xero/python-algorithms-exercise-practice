# code based on https://github.com/dev-xero/java-algorithms-exercise-practice

"""main.py
   Python code implementation of some exercises presented in chapter 1.1
   of the algorithms book
"""

# ---------------------------------------------------------------------------------------------------------


import random as generator


# ---------------------------------------------------------------------------------------------------------


class Fibonacci:
    """Class containing two implementations of fibonacci sequence sum algorithms"""
    @staticmethod
    def fib(n: int) -> int:
        """Recursive implementation"""
        if n == 0:
            return 0

        if n == 1:
            return 1

        return Fibonacci.fib(n - 2) + Fibonacci.fib(n - 1)

    @staticmethod
    def fast_fib(n: int, cache: {int: int}) -> int:
        """Fibonacci sequence algorithm utilizing dynamic programing and memoization"""
        if n == 0:
            cache[n] = 0
            return 0

        if n == 1:
            cache[n] = 1
            return 1

        cache[n] = cache[n - 2] + cache[n - 1]
        return cache[n]


# ---------------------------------------------------------------------------------------------------------


def is_between_zero_and_one(x: float, y: float) -> bool:
    """Returns true if the floats x and y exist between 0 and 1, false otherwise"""
    return (0 < x < 1) and (0 < y < 1)


# ---------------------------------------------------------------------------------------------------------


def to_binary_string(n: int) -> str:
    """Returns a string representing the binary form of an integer"""
    if n == 1:
        return "1"

    return to_binary_string(n // 2) + str(n % 2)


# ---------------------------------------------------------------------------------------------------------


def print_two_dm_boolean_array(the_array: [[bool]]) -> None:
    """Prints the contents of a boolean two-dimensional array, '*' for true and ' ' otherwise"""
    for row in the_array:
        for col in row:
            if col:
                print("* ", end="")

            else:
                print(" ", end="")

        print()


# ---------------------------------------------------------------------------------------------------------


def print_two_dm_int_array(the_array: [[int]]) -> None:
    """Prints the formatted contents of a two-dimensional int array"""
    for row in the_array:
        for col in row:
            print(f'[{col}]', end="")

        print()


# ---------------------------------------------------------------------------------------------------------


def print_int_array(the_array: [int]) -> None:
    """Prints the formatted contents of an int array"""
    for item in the_array:
        print(f'{item} ', end="")


# ---------------------------------------------------------------------------------------------------------


def matrix_transposition(the_matrix: [[int]]) -> [[int]]:
    """Returns the transpose of a matrix"""
    rows: int = len(the_matrix)
    cols: int = len(the_matrix[0])  # the number of columns remain constant

    transposed_matrix = [[0] * rows for _ in range(cols)]

    for i in range(cols):
        for j in range(rows):
            transposed_matrix[i][j] = the_matrix[j][i]

    return transposed_matrix


# ---------------------------------------------------------------------------------------------------------


def lg(n: float) -> int:
    """Returns the largest integer not larger than lg(n)"""
    if n <= 1:
        return 0

    return lg(n / 2) + 1


# ---------------------------------------------------------------------------------------------------------


def fact(n: int) -> int:
    """Returns the computed factorial of an integer"""
    if n == 1:
        return 1

    return n * fact(n - 1)


# ---------------------------------------------------------------------------------------------------------


def binary_search(key: int, the_array: [int]) -> int:
    """Calls _rank() to binary search the_array"""
    return _rank(key, sorted(the_array), 0, len(the_array) - 1)  # works best on sorted arrays


def _rank(key: int, the_array: [int], min_index: int, max_index: int) -> int:
    """Returns the index of the key if present, -1 if not"""
    if min_index > max_index:
        return -1

    mid_index: int = min_index + (max_index - min_index) // 2

    if the_array[mid_index] == key:
        return mid_index

    if the_array[mid_index] > key:
        return _rank(key, the_array, min_index, mid_index - 1)

    return _rank(key, the_array, mid_index + 1, max_index)


# ---------------------------------------------------------------------------------------------------------


def brute_force_search(key: int, the_array: [int], index: int) -> int:
    """Returns the index of the key if present, otherwise -1 using brute force search"""
    if index == len(the_array):
        return -1

    if the_array[index] == key:
        return index

    return brute_force_search(key, the_array, index + 1)


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_x: float = 0.1
    test_y: float = 0.5

    test_two_dm_boolean_array = [
        [True, False],
        [False, True],
        [True, False]
    ]

    test_two_dm_int_array = [
        [1, 7, 4],
        [6, 5, 2]
    ]

    test_int_array = [5, 7, 6, 9, 3, 8, 2, 4, 1, 10]

    test_int_matrix = [[0] * 2 for _ in range(3)]

    cache = {}

    for i in range(3):
        for j in range(2):
            test_int_matrix[i][j] = generator.randint(0, 9)

    print(is_between_zero_and_one(test_x, test_y))
    print(to_binary_string(8))
    print()

    print_two_dm_boolean_array(test_two_dm_boolean_array)
    print()

    print_two_dm_int_array(test_two_dm_int_array)
    print()

    print_int_array(test_int_array)
    print()

    print()
    print("- Matrix")
    print_two_dm_int_array(test_int_matrix)

    print()
    print("- Transposition")
    print_two_dm_int_array(matrix_transposition(test_int_matrix))

    print()
    print(f"floor of lg(128): { lg(128) }")

    print()
    print("- Dynamic Programming and Memoization Fib")

    for i in range(40):
        print(Fibonacci.fast_fib(i, cache))

    print()
    print("- Recursive Fib")

    for i in range(40):
        print(Fibonacci.fib(i))

    print()
    print(f"7!: { fact(7) }")

    print()
    print("- Sorted Array")
    print_int_array(sorted(test_int_array))

    print()
    print()

    print("- Binary Search: key = 4")
    print(f"index: { binary_search(4, test_int_array) }")

    print()
    print("- Brute Force Search: key = 8")
    print(f"index: { brute_force_search(8, sorted(test_int_array), 0) }")


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
