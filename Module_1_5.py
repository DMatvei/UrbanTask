immutable_var = 1, 'aboba', 3.14, False
print(immutable_var)

# Следующий код не имеет смысла, так как в кортеже хранятся ссылки на конкретный объект,
# а попыткой изменить ссылку на другой объект, мы вызовем ошибку в связи
# с изменением неизменяемой ссылки в кортедже
# immutable_var[0] = 10

mutable_list = [1, 'aboba', 3.14, False]
print(mutable_list)
mutable_list[0] = True
print(mutable_list)