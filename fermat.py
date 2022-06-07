from random import randint


# implementacao baseada na seção Algorithm de https://en.wikipedia.org/wiki/Fermat_primality_test
def fermat_test(n: int, rounds_of_testing: int = 100) -> bool:
    # algoritmo projetado para n > 3, porem como 2 e 3 podem ser gerados, o teste é realizado
    if n in [2, 3]:
        return True
    # numeros menores que 2 ou pares nao sao primos
    if n < 2 or n % 2 == 0:
        return False

    for _ in range(rounds_of_testing):
        # obter um numero inteiro aleatorio no intervalo [2, n - 2]
        a = randint(2, n - 2)

        # checa se a^(n-1) % n != 1; caso seja verdade o numero é composto
        if pow(a, n - 1, n) != 1:
            return False

    # o numero n provavelmente e primo
    return True
