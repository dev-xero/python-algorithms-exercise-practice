def is_between_zero_and_one(x: float, y: float) -> bool:
    return (0 < x < 1) and (0 < y < 1)


def main():
    test_x: float = 0.1
    test_y: float = 0.5

    print(is_between_zero_and_one(test_x, test_y))


if __name__ == "__main__":
    main()
