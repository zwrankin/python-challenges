def _reverse(s: str):
	return s[::-1]


def is_palindrome(s: str):
	assert isinstance(s,  str), "Please enter a string"
	return s == _reverse(s)
	