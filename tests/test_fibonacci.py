from pychallenge.fibonacci.fibonacci import fibonacci
import codecov


def test_fib_10():
    assert (fibonacci(10) == 55)


def test_fib_not_20():
    assert (fibonacci(20) != 20)
