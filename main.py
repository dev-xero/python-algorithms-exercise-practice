def is_between_zero_and_one(x: float, y: float) -> bool:
    return (0 < x < 1) and (0 < y < 1)


def to_binary_string(n: int) -> str:
    if n == 1:
        return "1"

    return to_binary_string(n // 2) + str(n % 2)


def main():
    test_x: float = 0.1
    test_y: float = 0.5

    print(is_between_zero_and_one(test_x, test_y))
    print(to_binary_string(8))


if __name__ == "__main__":
    main()
