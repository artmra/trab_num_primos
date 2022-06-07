import time
from math import gcd
import random


# algoritmo baseado no contido em https://pt.wikipedia.org/wiki/Blum_Blum_Shub
class BlumBlumShub:
    def __init__(self, x0: int = 1, p: int = 3141592653589771, q: int = 2718281828459051, generate_x0: bool = True) -> None:
        # se x0 n tiver sido providenciado, gera um
        if generate_x0:
            x0 = random.getrandbits(64)
        # aplica restrições para os valores de m
        if p == q or p % 4 != 3 or q % 4 != 3 or gcd(p, q) != 1:
            raise ValueError("Valores incorretos para p e q; p e q devem ser diferentes, congruentes a 3 e "
                             "relativamente "
                             "primos.")
        # salva m
        self.m = p * q
        # salva x0
        self.state = x0
        # inicializa o gerador
        self.next_state()

    # gera o proximo estado, seguindo a regra de xn = (xn-1 ^ 2) mod m
    def next_state(self) -> int:
        self.state = pow(self.state, 2, self.m)
        return self.state

    # gera o proximo estado e mapeia o resultado para 0 ou 1, gerando assim um bit
    def next_bit(self) -> int:
        return self.next_state() % 2

    # gera uma sequencia de bit aleatoria, deslocando a o ultimo bit gerado para a esquerda sucessivamente ate
    # que o numero de bits desejado tenha sido gerado; esse metodo tambem conta o tempo de execucao a fim de
    # fornecer dados para o relatorio
    def generate_and_record_time(self, size: int = 1) -> (int, int):
        start = time.time()
        n = 0
        for _ in range(size):
            n = (n << 1) | self.next_bit()
        return n, time.time() - start

    # gera uma sequencia de bit aleatoria, deslocando a o ultimo bit gerado para a esquerda sucessivamente ate
    # que o numero de bits desejado tenha sido gerado;
    def generate(self, size: int = 1) -> int:
        n = 0
        for _ in range(size):
            n = (n << 1) | self.next_bit()
        return n

    # feito para ajudar no processo de gerar números primos; esse metodo não garante que um número é primo(exceto no
    # caso de n = 2), porém garante que o número não é par, o que naturalmente quebra um dos requisitos para um número
    # ser primo(quando esse numero nao é 2, claro)
    def generate_prime(self, size: int = 1) -> int:
        n = self.generate(size)
        if n != 2:
            return n | 1
        return n

    # apenas pra printar as coisas bunitinho
    def get_algorithm_name(self) -> str:
        return 'Blum Blum Shub'