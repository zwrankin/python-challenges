from pychallenge.palindrome.palindrome import _reverse, is_palindrome
import pytest


def test_reverse():
    assert _reverse("rat") == "tar"
    assert _reverse("a") == "a"
    assert _reverse("") == ""


def test_palindrome():
    assert is_palindrome("car") is False
    assert is_palindrome("racecar") is True
    assert is_palindrome("rac-%^%-car") is True


def test_palindrome_typing():
    with pytest.raises(Exception) as e_info:
        is_palindrome(123)
    with pytest.raises(Exception) as e_info:
        is_palindrome(None)
    with pytest.raises(Exception) as e_info:
        is_palindrome(_reverse)
