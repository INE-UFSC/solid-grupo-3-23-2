"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

=> A dependência de StatsReporter é de uma classe concreta (Player), não uma interface abstrata(como deveria ser).
=> Para solucionar o problema, deveria ser criada uma interface abstrata, chamada Personagem.
=> Usando o mecanismo de herança, tal impasse é solucionado, agora tem-se duas classes dependendo de uma interface abstrata.

"""
from abc import ABC, abstractmethod


class IPersonagem(ABC):

    @abstractmethod
    def hp(self):
        pass

    @abstractmethod
    def name(self):
        pass


class Player:
    def __init__(self, name):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    @property
    def hp(self):
        return self.__hp

    @property
    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self, char: IPersonagem):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
