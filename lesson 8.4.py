def val_checker1(l_func):
    def val_checker2(func):
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f"wrong val {num}")

        return wrapper

    return val_checker2


@val_checker1(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(5)
except ValueError as err:
    print(err)
