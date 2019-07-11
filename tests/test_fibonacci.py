from pychallenge.fibonacci.fibonacci import fibonacci
import pytest


def test_fibonacci():
    assert fibonacci(10) == 55
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_fibonacci_val():
    with pytest.raises(Exception) as e_info:
        fibonacci(-1)
    with pytest.raises(Exception) as e_info:
        fibonacci(1.5)
    with pytest.raises(Exception) as e_info:
        fibonacci(None)
