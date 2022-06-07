from random import randint


# implementacao baseada no pseudo codigo em https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# rounds_of_testing devido ao fato desse ser o numero padrao usado pelo openssl, como informado aqui
# https://www.openssl.org/docs/man1.1.1/man1/openssl-prime.html
def miller_rabin_test(n: int, rounds_of_testing: int = 100) -> bool:
    # algoritmo projetado para n > 3, porem como 2 e 3 podem ser gerados, o teste é realizado
    if n in [2, 3]:
        return True
    # numeros menores que 2 ou pares nao sao primos
    if n < 2 or n % 2 == 0:
        return False
    # decompoe o numero, de forma que o mesmo possa ser escrito como 2^s * d + 1;
    # para tal deve-se obter s e d com base em n-1
    s, d = decompose(n - 1)

    for _ in range(rounds_of_testing):
        # Pegue um valor aleatorio no intervalo [2, n-2]
        a = randint(2, n - 2)
        # x = a^d mod n
        x = pow(a, d, n)
        # checa se x == 1 ou x == -1
        if x in [1, n - 1]:
            continue

        loop_again = False
        for _ in range(s - 1):
            # checa se x^2 mod n == n - 1; se for verdade quebra o loop e atribui True a loop_again
            if pow(x, 2, n) == n - 1:
                loop_again = True
                break
        if not loop_again:
            # o numero não e primo
            return False
    # o numero provavelmente e primo
    return True


# decompoe um numero n qualquer; realiza a divisao com deslocamento a esquerda pois a condicao do while garante que
# n sera par
def decompose(n: int) -> (int, int):
    s = 0
    while n % 2 == 0:
        s += 1
        # divide por 2
        n = n >> 1
    return s, n
