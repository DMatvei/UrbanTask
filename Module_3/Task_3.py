
def print_params(a = None, b = None, c = None):
    print(a, b, c)

print_params()
print_params(1)
print_params(c = [1, 2, 3])
print_params(1, 2, 3)

values_list = [1, "e", 3.14]
print_params(*values_list)

values_dict = {'a': 2.7, 'b': 'pi', 'c': True}
print_params(**values_dict)

values_list_2 = values_list[-1:0:-1]
print_params(*values_list_2, 42)

