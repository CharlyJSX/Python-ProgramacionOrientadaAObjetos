class Drink:
    def __init__(self, name):
        self.__name = name
    def getDetail(self):
        return "la bebida es: " + self.__name
    
class Product:
    def __init__(self, cost, price):
        self.cost = cost
        self. price = price
    def getGain(self):
        return self.price - self.cost

class Beer(Drink, Product):

    Count = 0

    def __init__(self, name, brand, alcohol, cost, price):
        Drink.__init__(self, name)
        Product.__init__(self, cost, price)
        self.__brand = brand
        self.__alcohol = alcohol
        Beer.Count += 1

    def getDetail(self, text = ""):
        return text + super().getDetail() + " de la marca: " + self.__brand + " con alcohol " + str(self.__alcohol) 

    @staticmethod
    def getClassInfo():
        return "Se han creado " + str(Beer.Count) + " objetos"

beer1 = Beer("Pale Ale", "Minerva", 4.5, 10, 20)
print(beer1.getDetail("Info: "))
print(beer1.getGain())




""" beer2 = Beer("Stout", "Minerva", 6, 12, 23)
print(beer2.getDetail())

print(Beer.Count)
print(Beer.getClassInfo()) """