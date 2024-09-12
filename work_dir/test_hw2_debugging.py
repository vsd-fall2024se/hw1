from hw2_debugging import merge_sort

def test_first():
    arr = [4, 6, 7, 24, 99, 65, 38, 25]
    sorted_arr = arr
    sorted_arr.sort()
    assert merge_sort(arr) == sorted_arr

def test_second():
    arr = [1,1,2,3,4,5,6,7,8,9]
    sorted_arr = arr
    sorted_arr.sort()
    assert merge_sort(arr) == sorted_arr

def test_third():
    arr = [9,8,7,6,5,4,3,2,1]
    sorted_arr = arr
    sorted_arr.sort()
    assert merge_sort(arr) == sorted_arr