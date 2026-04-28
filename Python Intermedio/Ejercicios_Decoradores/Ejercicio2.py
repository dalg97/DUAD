def decorator1(func):
    def wrapper(*args):
        try:
            for arg in args:
                if not isinstance(arg, (int,float)):
                    raise TypeError(f"{arg} is not a number")
            return func(*args)
        except Exception as e:
            print(f"{e}")
    return wrapper

@decorator1
def suma(a,b,c):
    result = a+b+c
    print(f"The sum is {result}")

suma(1,2,3)
suma(5,1,"a")
    