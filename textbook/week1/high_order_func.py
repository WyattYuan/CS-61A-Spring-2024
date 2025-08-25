def call_func(times, func):
    for i in range(times):
        func()


def hello():
    print("Hello, world!")


# call_func(3,hello)


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def improve(update, close, guess=1):
    iterations = 0
    while not close(guess):
        guess = update(guess)
        iterations += 1
        if iterations > 1100:
            break
    return guess


def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)

    return update


def find_root(f, df, guess=1):
    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero, guess)


# print(find_root(lambda x: x**2 - 4, lambda x: 2*x,2))


def curried_pow(x):
    def h(y):
        return pow(x, y)

    return h


# print(curried_pow(2)(3))


def curry2(f):
    """Return a curried version of the given two-argument function."""

    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g


def simple_decorator(func):
    def wrapper(*args):
        print("函数执行前的操作")
        result = func(*args)
        print("函数执行后的操作")
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f"你好，{name}！")

greet("小明")  
# 输出:
# 函数执行前的操作
# 你好，小明！
# 函数执行后的操作
