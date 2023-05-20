# Python Algorithms Exercise Practice
🐍 Exercise solutions for chapter 1.1 written in Python

## Algorithms Implemented
1. is_between_zero_and_one()
2. to_binary_string()
3. print_two_dm_boolean_array()
4. print_two_dm_int_array()
5. print_int_array()
6. matrix_transposition()
7. lg()
8. Fibonacci.fib()
9. Fibonacci.fast_fib()
10. fact()
11. binary_search()

## Code Examples
One interesting implementation is this algorithm to compute fibonacci sequences (exercise 1.1.19). It runs in O(1) time provided that the cache contains the previous two sequences. Generating the previous sequences is usually done using loops.
```python3
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
```

## Java Implementation
These were originally implemented in Java. You can find the source [here](https://github.com/dev-xero/java-algorithms-exercise-practice)
