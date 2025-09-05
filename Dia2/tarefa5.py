class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    def falar(self):
        return "Som de animal genérico"

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Au au!"

# gato = Gato("Mingau", 3)
# cachorro = Cachorro("Rex", 5)

# print(gato.apresentar())       # Olá, meu nome é Mingau e tenho 3 anos.
# print(gato.falar())            # Miau!

# print(cachorro.apresentar())   # Olá, meu nome é Rex e tenho 5 anos.
# print(cachorro.falar())        # Au au!
