
# def add(*args): #this allows you to pass in any number of values to this function
#     sum = 0
#     print(args[0])
#     print(type(args))
#     for n in args:
#         sum += n
#     return sum
#
# print(add(1,2,3,4))
# print(add(7,134534,45,6,567,76,756,435,675,756,7536,7,5685,5426,437,568,56))

#now time to show off keyword arguments or kwargs

def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)



class Car:

    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.engine = kwargs.get("engine")
        #using get func with a dictionary will just return None if there is no argument provided to initialize it

my_car = Car(make="nissan", model="gtr", engine="VQ_v6")
print(my_car.model)
print(my_car.engine)