# # *args for many positional arguments
# def add(*args):
#     """Returns the SUM of any number of integer inputs"""
#     # print(args)
#     # # type of args
#     # print(type(args))
#     # # print first element of the input (args) tuple
#     # print(args[0])
#     total = 0
#     for number in args:
#         total += number
#     return total
#
#
# # **kwargs for many keyword arguments
# def calculate(n, **kwargs):
#     """Returns the Result of any number of number inputs with their specified operation"""
#     # print(kwargs)
#     # print(type(kwargs))
#     # print element for key 'add' in the input (kwargs) dict
#     # print(kwargs["add"])
#     result = 0
#     for (key, element) in kwargs.items():
#         if key == "add":
#             n += element
#         elif key == "multiply":
#             n *= element
#         elif key == "divide":
#             n /= element
#         elif key == "minus":
#             n -= element
#         else:
#             n = 0
#     result = n
#     return n
#
#
# print(add(1.0, 2.1, 3, 4, 5, 6, 7))
# print(calculate(1, add=3, multiply=2))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

    def print(self):
        print(f"Make : {self.make}")
        print(f"Model : {self.model}")
        print(f"Color : {self.color}")
        print(f"Seats : {self.seats}")


my_car = Car(make="Nissan", model="SkyLine")
my_car.print()
