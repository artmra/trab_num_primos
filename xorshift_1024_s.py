import random


class Xorshift1024s:
    # constantes propostas em https://vigna.di.unimi.it/ftp/papers/xorshift.pdf
    A = 31
    B = 11
    C = 30
    MULTIPLIER = 1181783497276652981

    def __init__(self, state: list = None) -> None:
        # verifica se a lista de estados proposta está de acordo com o esperado; se ela nao tiver sido passada, gera
        # uma
        if state is not None:
            if len(state) != 16:
                raise ValueError("A lista de estados deve conter 1024 bits")
            for s in state:
                if type(s) != int:
                    raise ValueError("O estado deve conter apenas numeros")
            self.state = state
        else:
            self.state = list()
            for _ in range(16):
                self.state.append(random.getrandbits(64))
        # index inicial
        self.index = 0

    # gera o proximo estado;
    def next_state(self) -> int:
        # recupera o ultimo index
        index = self.index
        # salva o ultimo conjunto de 64 bits usados para gerar um novo valor
        s = self.state[index]
        # atualiza o index de maneira circular
        index = (index + 1) % 15
        # obtem o conjunto de bits que sera utilizado como base para gerar a nova sequencia
        t = self.state[index]
        # realiza A deslocamentos a esquerda e B deslocamentos a direita em t; cada um dos deslocamentos e seguido
        # da realizacao de um xor do novo valor obtido com o deslocamento com o valor original pre deslocamento
        t ^= t << self.A;
        t ^= t >> self.B;
        # realiza C deslocamentos a direita em s, e em seguida realiza o xor desse novo valor com o valor original de s;
        # por fim é realizado o xor entre o valor obtido e t
        t ^= s ^ (s >> self.C)
        # lembra do ultimo estado
        self.state[index] = t
        # atualiza o ultimo index
        self.index = index
        return t * self.MULTIPLIER

    # gera o proximo estado e mapeia o resultado para 0 ou 1, gerando assim um bit
    def next_bit(self) -> int:
        return self.next_state() % 2

    # gera uma sequencia de bit aleatoria, deslocando a o ultimo bit gerado para a esquerda sucessivamente ate
    # que o numero de bits desejado tenha sido gerado
    def generate(self, size: int = 1) -> int:
        n = 0
        for _ in range(size):
            n = (n << 1) | self.next_bit()
        return n

    # feito para ajudar no processo de gerar números primos; esse metodo não garante que um número é primo(exceto no
    # caso de n = 2), porém garante que o número não é par, o que naturalmente quebra um dos requisitos para um número
    # ser primo
    def generate_prime(self, size: int = 1) -> int:
        n = self.generate(size) | 1
        if n != 2:
            return n | 1
        return n
