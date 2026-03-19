def dividef(n1: float, n2: float) -> float:
    '''
    Função que retorna a divisão de dois números (inteiros ou reais).

    :param n1: número 1 (int ou float)
    :param n2: número 2 (int ou float)
    :return: divisão de n1 / n2 (float)

    Exemplo:
    >>> dividef(6, 3)
    2.0
    >>> dividef(5.0, 2.0)
    2.5
    '''
    if n2 == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return n1 / n2


def main():
    assert dividef(6, 3) == 2.0, "Erro: 6 / 3 deveria ser 2.0"
    assert dividef(5.0, 2.0) == 2.5, "Erro: 5.0 / 2.0 deveria ser 2.5"
    assert dividef(-6, 3) == -2.0, "Erro: -6 / 3 deveria ser -2.0"
    assert dividef(0, 5) == 0.0, "Erro: 0 / 5 deveria ser 0.0"
    assert dividef(1.5, 0.5) == 3.0, "Erro: 1.5 / 0.5 deveria ser 3.0"
    try:
        dividef(5, 0)
        assert False, "Erro: deveria ter lançado ValueError"
    except ValueError:
        pass
    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    main()

