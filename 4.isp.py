"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão.


=> O problema apresentado é que todas as outras interfaces dependem de uma interface genérica,
=> que muitas vezes não utilizarão todos os métodos declarados em IJanela.
=> Para a solução, deve-se fracionar a interface IJanela em interfaces menores, especificadas.

"""
from abc import ABC, abstractmethod

class IJanela(ABC):

    @abstractmethod
    def fechar(self):
        raise NotImplementedError

class IJanelaDimensionavel(ABC):

    @abstractmethod
    def minimizar(self):
        raise NotImplementedError

    @abstractmethod
    def maximizar(self):
        raise NotImplementedError

class IJanelaMostraMenu(ABC):

    @abstractmethod
    def mostrar_menu(self):
        raise NotImplementedError


class JanelaTamanhoFixo(IJanela, IJanelaMostraMenu):

    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass


class JanelaSemMenu(IJanela, IJanelaDimensionavel):

    def maximizar(self):
        pass

    def minimizar(self):
        pass

    def fechar(self):
        pass


