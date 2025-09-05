class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nome}, {self.idade} anos - Fala: {self.falar()}"

class Gato(Animal):
    def falar(self):
        return

class Cachorro(Animal):
    def falar(self):
        return
    
class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        if isinstance(animal, Animal):
            self.animais.append(animal)
        else:
            print("Somente instâncias da classe Animal (ou subclasses) podem ser adicionadas.")

    def listar_animais(self):
        return [str(animal) for animal in self.animais]

    def filtrar_por_tipo(self, tipo):
        return [animal for animal in self.animais if isinstance(animal, tipo)]
