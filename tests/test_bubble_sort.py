from pychallenge.sort.bubble import bubble_sort


def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([0]) == [0]
    assert bubble_sort([-1, 0, 1]) == [-1, 0, 1]
    assert bubble_sort([1, 0, -1]) == [-1, 0, 1]
    assert bubble_sort(["a", "c", "b"]) == ["a", "b", "c"]
    assert bubble_sort(["aardvark", "cat", "banana"]) == ["aardvark", "banana", "cat"]
    assert bubble_sort('aardvark') == sorted('aardvark')
