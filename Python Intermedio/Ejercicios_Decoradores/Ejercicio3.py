from datetime import date

class User:
    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def show_date_of_birth(self):
        today = date.today()
        years = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years
    
def decorator1(func):
    def wrapper(User,*args):
        try:
            if User.show_date_of_birth < 18:
                raise ValueError(f"It is less than 18")
            else:
                return func(User,*args)
        except Exception as e:
            print(e)
    return wrapper

@decorator1
def check_age(User):
    print("It is allowed")

diego = User(date(1995,5,12))
andres = User(date(2010,8,1))
check_age(diego)
check_age(andres)