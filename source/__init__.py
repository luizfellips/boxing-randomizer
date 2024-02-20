from source import BoxingBot
import random

class Initializer:
    def __init__(self) -> None:
        self.boxingBot = BoxingBot.BoxingBot()

        while True:
            print(f'[1] Gerar combinação de socos \n[2]Sair')
            operation = int(input('\n>'))
            if operation == 1:
                punches = int(input("Quantos tipos de soco? "))
                dodges = int(input("Quantos tipos de defesa? "))
                
                print(f'Combinação 1: {self.getCombination(punches, dodges)}')
            else:

                break

    def getCombination(self, punches, dodges):
        punches = self.boxingBot.getPunchesCombination(punches)
        dodges = self.boxingBot.getDodgesCombination(dodges)
        combined_list = punches + dodges
        random.shuffle(combined_list)

        return combined_list