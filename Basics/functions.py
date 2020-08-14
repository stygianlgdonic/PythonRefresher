# define a basic function
def func1():
    print("sample function")


# function that takes arguments
def func2(arg1, arg2):
    print(arg1, arg2)


# function that returns a value
def sqaure(x):
    return x * x


# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result *= num
    return result


# function with variable number of arguments
def avg(*args):
    count = 0
    total = 0
    for i in args:
        total += i
        count += 1

    return total / count


if __name__ == "__main__":
    func1()
    func2("Hello", 123)
    print(sqaure(12))
    print(power(2))
    print(power(2, 3))
    print(avg(1, 2, 3, 4, 5))
