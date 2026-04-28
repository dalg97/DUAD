def decorator1(func):
    def wrapper(a,b):
        print(f"{a} and {b} are the parameters in the decorator")
        result = func(a,b)
        return result
    return wrapper

@decorator1
def print_parameters(a,b):
    print(f"{a} and {b} are the parameters inside the function")

print_parameters(5,2)
