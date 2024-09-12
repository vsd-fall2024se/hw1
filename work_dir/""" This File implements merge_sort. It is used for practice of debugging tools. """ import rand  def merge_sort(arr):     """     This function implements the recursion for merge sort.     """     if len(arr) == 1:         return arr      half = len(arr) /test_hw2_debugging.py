from hw2_debugging import merge_sort

def test_first():
    arr = [4, 6, 7, 24, 99, 65, 38, 25]
    assert merge_sort(arr) == [4, 6, 7, 24, 25, 38, 65, 99]

def test_second():
    arr = [1,1,2,3,4,5,6,7,8,9]
    assert merge_sort(arr) == [1,1,2,3,4,5,6,7,8,9]

def test_third():
    arr = [9,8,7,6,5,4,3,2,1]
    assert merge_sort(arr) == [1,2,3,4,5,6,7,8,9]
