# code based on https://github.com/dev-xero/java-algorithms-exercise-practice

"""main.py
    Python code implementation of some exercises presented in chapter 1.1
    of the algorithms book
"""

# ---------------------------------------------------------------------------------------------------------


import random as generator


# ---------------------------------------------------------------------------------------------------------


def is_between_zero_and_one(x: float, y: float) -> bool:
    """Return true if the floats x and y exist between 0 and 1 else otherwise"""
    return (0 < x < 1) and (0 < y < 1)


# ---------------------------------------------------------------------------------------------------------


def to_binary_string(n: int) -> str:
    """Return a string representing the binary form of an integer"""
    if n == 1:
        return "1"

    return to_binary_string(n // 2) + str(n % 2)


# ---------------------------------------------------------------------------------------------------------


def print_two_dm_boolean_array(the_array: [[bool]]) -> None:
    """Prints the content of a boolean two-dimensional array, '*' for true and ' ' otherwise"""
    for row in the_array:
        for col in row:
            if col:
                print("* ", end="")

            else:
                print(" ", end="")

        print()


# ---------------------------------------------------------------------------------------------------------


def print_two_dm_int_array(the_array: [[int]]) -> None:
    """Print the formatted contents of an int two-dimensional array"""
    for row in the_array:
        for col in row:
            print(f'[{col}]', end="")

        print()


# ---------------------------------------------------------------------------------------------------------


def print_int_array(the_array: [int]) -> None:
    """Print the formatted contents of an int array"""
    for item in the_array:
        print(f'{item} ', end="")


# ---------------------------------------------------------------------------------------------------------


def matrix_transposition(the_matrix: [[int]]) -> [[int]]:
    rows = len(the_matrix)
    cols = len(the_matrix[0])  # the number of columns remain constant

    transposed_matrix = [[0] * rows for _ in range(cols)]

    for i in range(cols):
        for j in range(rows):
            transposed_matrix[i][j] = the_matrix[j][i]

    return transposed_matrix


# ---------------------------------------------------------------------------------------------------------


def main():
    """For testing"""
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

    test_int_matrix = [[0] * 2 for _ in range(3)]
    for i in range(3):
        for j in range(2):
            test_int_matrix[i][j] = generator.randint(0, 9)

    test_int_array = [5, 7, 6, 9, 3, 8, 2, 4, 1, 10]

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


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
