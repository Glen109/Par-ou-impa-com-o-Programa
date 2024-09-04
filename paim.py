import random

class Simuladordepoui:
    def lançar(self, vezes=1):
        return random.randint(1, 10)

def main():
    print("Bem-vindo ao Simulador de Par ou Ímpar!")
    usuario = input("Digite P (para Par) ou I (Ímpar): ").upper()
    dedos = int(input("Digite o número de dedos que vai jogar: "))

    resultado_dado = Simuladordepoui.lançar(1)
    soma_total = resultado_dado + dedos

    print(f"Resultado da Soma Total: {soma_total}")
    if (soma_total % 2 == 0 and usuario == 'P') or (soma_total % 2 != 0 and usuario == 'I'):
        print("Parabéns, você ganhou!")
    else:
        print("Você perdeu...")

if __name__ == "__main__":
    main()
