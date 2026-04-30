def decorator1(func):
    def wrapper(a,b):
        print(f"{a} and {b} are the parameters in the decorator")
        result = func(a,b)
        print(f"Result: {result}")
        return result
    return wrapper

@decorator1
def print_parameters(a,b):
    return f"The order of the parameter has changed: {b} and {a}"

print_parameters(5,2)
