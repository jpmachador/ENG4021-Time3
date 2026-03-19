def subtraif(n1: float, n2: float) -> float:
    '''
    Função que retorna a subtração de dois números (inteiros ou reais).

    :param n1: número 1 (int ou float)
    :param n2: número 2 (int ou float)
    :return: subtração de n1 - n2 (float)

    Exemplo:
    >>> subtraif(5, 3)
    2
    >>> subtraif(2.5, 1.5)
    1.0
    '''
    return n1 - n2


def main():
    assert subtraif(5, 3) == 2, "Erro: 5 - 3 deveria ser 2"
    assert subtraif(2.5, 1.5) == 1.0, "Erro: 2.5 - 1.5 deveria ser 1.0"
    assert subtraif(-1.5, 4.5) == -6.0, "Erro: -1.5 - 4.5 deveria ser -6.0"
    assert subtraif(0, 5) == -5, "Erro: 0 - 5 deveria ser -5"
    assert subtraif(5, 0) == 5, "Erro: 5 - 0 deveria ser 5"
    assert subtraif(1.1, 1.1) == 0.0, "Erro: 1.1 - 1.1 deveria ser 0.0"
    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    main()
