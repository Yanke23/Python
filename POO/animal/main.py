from mamifero import Mamifero
from ave import Ave
from zoologico import Zoologico

def main():
    zoo = Zoologico("ZooTech")

    leao = Mamifero("Simba", 5, "Leão Africano", "Amarelo")
    urso = Mamifero("Baloo", 8, "Urso Pardo", "Marrom")
    pinguim = Ave("Kowalski", 3, "Pinguim Imperador", False)
    aguia = Ave("Careca", 4, "Águia Americana", True)

    zoo.adicionar_animal(leao)
    zoo.adicionar_animal(urso)
    zoo.adicionar_animal(pinguim)
    zoo.adicionar_animal(aguia)

    zoo.relatorio()
    zoo.alimentar_animais()

if __name__ == "__main__":
    main()