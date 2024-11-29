
list_types = (dict, list, tuple, set )
list_num_types = (int, float)




def calculate_structure_sum(data):
    sum_result = 0

    for i in data:
        if isinstance(i, list_types):
            if isinstance(i, dict):
                send_data = i.items()
                sum_result += calculate_structure_sum(send_data)
            else:
                sum_result += calculate_structure_sum(i)
        elif isinstance(i, list_num_types):
            sum_result += i
        elif isinstance(i, str):
            sum_result += len(i)

    return sum_result


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
