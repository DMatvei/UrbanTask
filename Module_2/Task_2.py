first_ = int(input("Введите первое число: "))
second_ = int(input("Введите второе число: "))
third_ = int(input("Введите третье число: "))

if first_ == second_ == third_:
    print(3)
elif first_ == second_ or first_ == third_ or second_ == third_:
    print(2)
else:
    print(0)
