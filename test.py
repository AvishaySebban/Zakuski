def shuffle(array):
    copy = list(array)
    shuffle_in_place(copy)
    return copy

def shuffle_in_place(array):
    import random
    array_len = len(array)
    assert array_len > 2, 'Array is too short to shuffle!'
    for index in range(array_len):
        swap = random.randrange(array_len - 1)
        swap += swap >= index
        array[index], array[swap] = array[swap], array[index]

array = list(range(10))
print array