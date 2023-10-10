"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar

-> A classe Animal não deve possuir a responsabilidade de salvar os dados
-> Deveria ser criada uma outra classe que vai gerenciar a persistência do Animal


class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    # salva no DB
    def save(self, animal: Animal):
        pass

"""

class Persistencia:

    def __init__(self):
        pass

    def save(self):
        pass


class Animal:
    def __init__(self, name: str, persistencia: Persistencia):
        self.name = name
        self.persistencia = persistencia
    
    def get_name(self) -> str:
        pass

    # salva no DB
    def save(self):
        self.persistencia.save()


