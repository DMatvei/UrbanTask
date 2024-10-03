input_number = int(input("Введите число от 3 до 20: "))

result = []


for first_num in range(1, 20):
    if first_num * 2 + 1 > input_number:
        break
    for second_num in range(first_num + 1, 20):
        sum_2_num = first_num + second_num
        if sum_2_num > input_number:
            break
        if input_number % sum_2_num == 0:
            result.append(first_num)
            result.append(second_num)



print(*result, sep='')
