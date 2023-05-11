# Study Drill - running functions in different ways

def func_call(func, args):
    func(args)

def print_something(something):
    print(f"the thing is {something}")

arg_to_func = "bicycle"

print_something(arg_to_func)
func_call(print_something, arg_to_func)

def square(num):
    print(f"the square is {num*num}")

number = 2
square(number)

func_call(square, number)

print_something(square)
func_call(print_something, square)


