class Car:
    def __init__(self, make, model, __top_speed):  # __top_speed is intended as private
        self.make = make
        self.model = model
        self.__top_speed = __top_speed

    def get_top_speed(self):  # Getter for __top_speed
        return self.__top_speed

    def set_top_speed(self, new_speed):  # Setter for __top_speed
        if new_speed > 0:
            self.__top_speed = new_speed
        else:
            print("Top speed must be positive.")

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Top Speed: {self.__top_speed} mph")


my_car = Car("Toyota", "Camry", 120)
my_car.display_info()

# Accessing public attributes directly
print(my_car.make)

# Attempting to access "private" attribute directly (will work due to name mangling, but discouraged)
# print(my_car.__top_speed) # This would raise an AttributeError if not for name mangling
print('not encourged this method: ', my_car._Car__top_speed)  # Accessing via name mangling (discouraged)
# print(my_car.__top_speed)
# Using getter and setter for controlled access
print(f"Current top speed: {my_car.get_top_speed()}")
my_car.set_top_speed(130)
my_car.display_info()
my_car.set_top_speed(-10)  # Demonstrates validation in setter


class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print(D.mro())
