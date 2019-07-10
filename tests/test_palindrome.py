import pytest
from pychallenge.palindrome.palindrome import _reverse, is_palindrome


def test_reverse():
	assert _reverse("rat") == "tar"
	assert _reverse("a") == "a"
	assert _reverse("") == ""


def test_palindrome():
	assert is_palindrome("car") == False
	assert is_palindrome("racecar") == True 
	assert is_palindrome("rac-%^%-car") == True 


def test_palindrome_typing():
	with pytest.raises(Exception) as e_info:
		is_palindrome(123)
	with pytest.raises(Exception) as e_info:
		is_palindrome(None)
	with pytest.raises(Exception) as e_info:
		is_palindrome(_reverse)
