def mask_sum(data, mask):
    res = 0
    for val, mask_val in zip(data, mask):
       if mask_val != 0:
            res += val
    return res


print(mask_sum([1, 2, 3], [0, 1, 1]))
