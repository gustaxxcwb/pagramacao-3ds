class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

# Cadastro de animais
animais = [Cachorro(), Gato()]

for animal in animais:
    print(f"{type(animal).__name__}: {animal.emitir_som()}")
