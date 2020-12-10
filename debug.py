import copy


def filter_array(arr):
    arr = copy.copy(arr)
    new_list = []
    for i in arr:
        if i > 0:
            new_list.append(i)

    return new_list


def print_result(arr):
    for i in arr:
        print(i)


list_ = [-1, 5, 9, 0, -2]
sorted_list = filter_array(list_)
print_result(sorted_list)
