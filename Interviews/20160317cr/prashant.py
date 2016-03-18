"""
Copyright (c) 2016 Marshall Farrier
license http://opensource.org/licenses/MIT

Find smallest unsorted portion of an array
of distinct values.
"""

import random

def unsorted_chunk(arr):
    unsorted_end_ix = find_first_unsorted(arr)
    if unsorted_end_ix < 0:
        return unsorted_end_ix, unsorted_end_ix
    unsorted_low_ix = unsorted_end_ix
    high_ix = unsorted_end_ix - 1
    unsorted_begin_ix = find_ix(arr, arr[unsorted_low_ix], 0, high_ix)
    for i in range(unsorted_end_ix + 1, len(arr)):
        if arr[i] < arr[high_ix]:
            unsorted_end_ix = i
            if arr[i] < arr[unsorted_low_ix]:
                unsorted_low_ix = i
                unsorted_begin_ix = find_ix(arr, arr[unsorted_low_ix], 0, unsorted_begin_ix)
        else:
            high_ix = i
    return unsorted_begin_ix, unsorted_end_ix

def find_first_unsorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return i
    return -1

def find_ix(arr, num, start_i, end_i):
    if start_i == end_i:
        return start_i
    mid_i = (start_i + end_i) // 2
    if num < arr[mid_i]:
        return find_ix(arr, num, start_i, mid_i)
    return find_ix(arr, num, mid_i + 1, end_i)

def running_sum(arr):
    tot = 0
    for item in arr:
        tot += item
        yield tot

def rand_sorted_arr(size, min_step, max_step):
    step_arr = [random.randint(min_step, max_step) for i in range(12)]
    return list(running_sum(step_arr))

def rand_distinct(size, n_vals):
    arr = range(size)
    random.shuffle(arr)
    return sorted(arr[:n_vals])

def _tst_bin_search():
    # generate a random array of distinct ints
    size = 12
    max_step = 7
    arr = rand_sorted_arr(size, 2, max_step)
    print(arr)
    # pick a random slice
    min_ix, max_ix = rand_distinct(size, 2)
    # find a number that fits in that slice
    mid_ix = random.randint(min_ix, max_ix)
    num = arr[mid_ix] - 1
    print(num)
    print(find_ix(arr, num, min_ix, max_ix))

def _tst_unsorted_chunk():
    # generate a random array of distinct ints
    size = 12
    max_step = 7
    arr = rand_sorted_arr(size, 1, max_step)
    print(arr)
    # pick a random slice
    min_ix, max_ix = rand_distinct(size, 2)
    # shuffle it
    #arr[min_ix:(max_ix + 1)] = random.shuffle(arr[min_ix:(max_ix + 1)])
    chunk = arr[min_ix:(max_ix + 1)]
    random.shuffle(chunk)
    arr[min_ix:(max_ix + 1)] = chunk
    print(chunk)
    print(min_ix, max_ix)
    print(arr)
    print(unsorted_chunk(arr))

if __name__ == '__main__':
    random.seed()
    _tst_unsorted_chunk()
