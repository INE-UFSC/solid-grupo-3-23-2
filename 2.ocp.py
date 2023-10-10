"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão

-> Nos exemplos em questão sempre que houver a necessidade de criar um novo animal ou novo tipo de cliente, seria necessária
a modificação da classe animal e discount. Tal situação poderia ser evitada implementando métodos genéricos na classe principal
e estabelecendo subclasses com implementações específicas do método
"""
'''class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        if self.name == 'lion':
            print('roar')
        elif self.name == 'mouse':
            print('squeak')
        else:
            print('...')

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)'''

from abc import ABC, abstractmethod

class Main():
    def __init__(self, animals: list):
        self.animals = animals

    def animal_sound(self):
        for animal in self.animals:
            animal.make_sound()

    def adicionar_animal(self, Tipo, nome):
        self.animals.append(Tipo(nome))

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        #detalhes do método
        pass

class Mouse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        #detalhes do método
        pass



"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            if self.customer == 'fav':
                return self.price * 0.2
            if self.customer == 'vip':
                return self.price * 0.4

