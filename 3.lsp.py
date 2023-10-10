"""
Liskov Substitution Principle

Uma subclasse deve ser substituível pela sua superclasse 

-> A classe Snake também herda de Animal, mas substitui o método leg_count() para 
imprimir uma mensagem em vez de retornar um valor (nesse caso, o número de pernas). Logo, a assinatura do método foi alterada,
fazendo com a classe Snake siga o LSP. A substituição de um método deve
 manter a mesma assinatura da classe base (Animal neste caso), para que as 
 instâncias de Snake possam ser usadas em qualquer lugar onde Animal é esperado.
 Assim um tipo Animal poderia ser substituido por Snake sem dar erros.
 Para corrigir, basta remover o método leg_count de Snake, pois assim ele vai utilizar o da classe 
 Animal mesmo, o qual já retorna 0 (a cobra tem 0 pernas)


class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

    def leg_count(self) -> int:
        return 0

class Lion(Animal):
    def __init__(self):
        super().__init__('lion')

    def leg_count(self):
        return 4

class Snake(Animal):
    def __init__(self):
        super().__init__('snake')

    def leg_count(self):
        print('I have no legs, dummy')


def animal_leg_count(animals: list):
    count = 0
    for animal in animals:
        count += animal.leg_count()
    return count

"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

    def leg_count(self) -> int:
        return 0

class Lion(Animal):
    def __init__(self):
        super().__init__('lion')

    def leg_count(self):
        return 4

class Snake(Animal):
    def __init__(self):
        super().__init__('snake')


def animal_leg_count(animals: list):
    count = 0
    for animal in animals:
        count += animal.leg_count()
    return count


