

class Car :
    def __init__(self ,brand,model):
        self.__brand = brand
        self.model= model
    
    def Full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get__brand(self):
        return self.__brand + "!"
    def fuel_type(self):
        return "petrol aur diseal"
    


    
class ElectricCar(Car):

    def __init__(self,brand,model,Battery_Size):
        super().__init__(brand,model)
        self.Battery_Size = Battery_Size
    
    def fuel_type(self):

        return "eLECTRIC Charge"




my_bmw_car = ElectricCar("teslaa","model S","800kWH")
# print(my_bmw_car.Full_name())
# print(my_bmw_car.get__brand()/])
print(my_bmw_car.fuel_type())


marcedes = Car("toyota","22 MODEL")
print(marcedes.fuel_type())

# my_result =Car( "toyota", "Corolla")
# print(my_result.brand)
# print(my_result.model)
# print(my_result.Full_name())
# my_car = Car("Bmw","Safari")
# print(my_car.brand)