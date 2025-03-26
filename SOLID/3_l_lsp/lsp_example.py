class Animal:
    def comer(self):
        print('O animal está comendo!')

    def andar(self):
        print('O animal está andando na jaula!')

class Felino(Animal):
    def lamber(self):
        print('O felino está lambendo seu pelo!')

class Leao(Felino):
    def rugir(self):
        print('O leão está rugindo!')

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()

renatinho = Pessoa()
animal = Animal()
felino = Felino()
leao = Leao()

renatinho.observa(animal)
renatinho.observa(felino)
renatinho.observa(leao)

# Herda as classes mais genéricas para não ter que repetir funções em classes mais específicas.