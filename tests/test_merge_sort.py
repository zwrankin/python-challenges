from pychallenge.sort.merge import merge_sort


def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([0]) == [0]
    assert merge_sort([-1, 0, 1]) == [-1, 0, 1]
    assert merge_sort([1, 0, -1]) == [-1, 0, 1]
    assert merge_sort(["a", "c", "b"]) == ["a", "b", "c"]
    assert merge_sort(["aardvark", "cat", "banana"]) == ["aardvark", "banana", "cat"]
    assert merge_sort('aardvark') == sorted('aardvark')
