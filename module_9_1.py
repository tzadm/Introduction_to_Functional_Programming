def apply_all_func(int_list, *functions):
    results = dict()
    for i in functions:
        value = i(int_list)
        results[i.__name__] = value

    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
