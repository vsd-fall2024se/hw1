"""
This is helper file for mergesort
"""
import subprocess


def random_array(arr):
    """
    This function generates a random array
    """
    shuffled_num = None
    for idx, _ in enumerate(arr):
        # for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[idx] = int(shuffled_num.stdout)
        # arr[i] = int(shuffled_num.stdout)
    return arr
