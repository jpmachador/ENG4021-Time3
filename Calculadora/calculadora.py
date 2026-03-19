from soma import soma
from subtracao import subtracao
from multiplicacao import multiplicacao
from divisao import divisao


def calculadora():
    print("============================")
    print("    Calculadora ENG4021")
    print("")
    print("   1 - Soma")
    print("   2 - Subtração")
    print("   3 - Multiplicação")
    print("   4 - Divisão")
    print("   0 - Sair")
    print("============================")

    while True:
        opcao = input("\nEscolha uma operação: ")

        if opcao == "0":
            print("Encerrando a calculadora.")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            continue

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {soma(a, b)}")
        elif opcao == "2":
            print(f"Resultado: {subtracao(a, b)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicacao(a, b)}")
        elif opcao == "4":
            try:
                print(f"Resultado: {divisao(a, b)}")
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    calculadora()
