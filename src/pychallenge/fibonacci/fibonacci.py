def fibonacci(n: int, a=0, b=1):
    assert isinstance(n, int)
    assert n >= 0

    if n == 0:  # edge case
        return a
    if n == 1:  # usual base case
        return b
    return fibonacci(n - 1, b, a + b)
