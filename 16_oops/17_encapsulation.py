# Declare the class
class Car(object):
    # Constructor
    def __init__(self, make, model) -> None:
        self.__make = make  # private attribute
        self.__model = model  # private attribute

    # Method to access make
    def get_make(self):
        return self.__make

    # Method to get access model
    def get_model(self):
        return self.__model

    # Method to start the engine
    def start_engine(self):
        # Call private methods sequentially
        self.__ignite_fuel()
        self.__start_spark_plugs()
        self.__start_crankshaft()
        print("Engine started.")

    # Private Method to ignite fuel
    def __ignite_fuel(self):
        print("Fuel ignited.")

    # Private Method to start spark plugs
    def __start_spark_plugs(self):
        print("Spark plugs started.")

    # Private Method to start crankshaft
    def __start_crankshaft(self):
        print("Crankshaft started.")


# Create an instance of the Car class
my_car = Car("Toyota", "Fortuner")


# Accessing attributes using getter methods
print(my_car.get_make())
print(my_car.get_model())


# # Trying to access private attributes directly
# # This will result in an AttributeError
# print(my_car.__make)
# print(my_car.__model)

# Calling methods to start the car's engine
my_car.start_engine()


# # Trying to access private attributes directly
# # This will result in an AttributeError
# print(my_car.__ignite_fuel)
# print(my_car.__start_spark_plugs)
# print(my_car.__start_crankshaft)
