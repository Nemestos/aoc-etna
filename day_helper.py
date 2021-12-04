def apply_func(func, liste):
    if func is not None:
        return list(map(func, liste))


def split_arr(array, separator):
    results = []
    j = 0
    for i in range(len(array)):
        x = array[i]
        if x == separator:
            results.append(array[j:i])
            j = i + 1
    if array[-1] != separator:
        results.append(array[j:])

    return results


def flatten(array):
    final = []
    for i in array:
        if type(i) == list:
            for j in i:
                final += [j]
        else:
            final += [i]
    return final
