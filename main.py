import time

from blum_blum_shub import BlumBlumShub
from xorshift_1024_s import Xorshift1024s
from fermat import fermat_test
from miller_rabin import miller_rabin_test

SIZE_OF_SEQUENCE = [40, 56, 80, 128, 168, 224, 512, 256, 1024, 2048, 4096]
NUMBER_OF_EXECUTIONS = 1000

# cria uma quantidade de numeros pseudo aleatorios igual a NUMBER_OF_EXECUTIONS para cada tamanho em SIZE_OF_SEQUENCE; quando a quantidade
# desejada de numeros de cada tamanho é gerada, o algoritmo calcula a media simples e imprime o resultado; para esses testes o algoritmo
# foi alterado de forma a guardar o tempo de execução para cada número gerado
def generate_pseudo_random_nums(use_blum_blum_shub: bool = True) -> None:
    for size in SIZE_OF_SEQUENCE:
        generator = BlumBlumShub() if use_blum_blum_shub else Xorshift1024s()
        average = 0
        for _ in range(NUMBER_OF_EXECUTIONS):
            _, execution_time = generator.generate_and_record_time(size)
            average += execution_time
        print('Tempo medio de execucao do algoritmo ', generator.get_algorithm_name(), ' para ', size, 'bits: ',
              average / 100)

# cria um numero cada tamanho em SIZE_OF_SEQUENCE usando uma combinacao de algorimos passada por paramentro para a funcao; quando um numero
# primo para cada tamanho é gerado o algoritmo imprime o tempo necessario para geralo e o numero em si
def generate_prime_nums(use_blum_blum_shub: bool = True, use_miller_rabin: bool = True) -> None:
    generator = BlumBlumShub() if use_blum_blum_shub else Xorshift1024s()
    primality_test = miller_rabin_test if use_miller_rabin else fermat_test
    test_name = 'teste de Miller Rabin' if use_miller_rabin else 'tesde de Fermat'
    for size in SIZE_OF_SEQUENCE:
        number, exec_time = generate_prime_num_of_n_bits(generator=generator, size=size, primality_test=primality_test)
        print('Tempo para gerar um primo de ', size, ' bits com o algoritmo ', generator.get_algorithm_name(), ' e o teste de primalidade ', test_name, ': ',
              exec_time, '. O numero gerado foi: ', number)

# funcao auxiliar que fica em loop criando numeros pseudo-aleatorios até que algum deles passe no teste de primalidade definido em
# primality_test
def generate_prime_num_of_n_bits(generator, size, primality_test) -> (int, int):
    start = time.time()
    n = 0
    generated_prime_number = False
    while not generated_prime_number:
        n = generator.generate_prime(size)
        generated_prime_number = primality_test(n)
    return n, time.time() - start


# apenas realiza os testes requisitados
if __name__ == '__main__':
    print('gerar numeros aleatorio com o algoritmo BBS')
    generate_pseudo_random_nums()
    print('\n\n\n\ngerar numeros aleatorio com o algoritmo xorshift')
    generate_pseudo_random_nums(use_blum_blum_shub=False)
    # print('\n\n\n\ngerar numeros aleatorio com o algoritmo BBS e teste de miller rabin')
    # generate_prime_nums(use_blum_blum_shub=True, use_miller_rabin=True)
    # print('\n\n\n\ngerar numeros aleatorio com o algoritmo BBS e teste de fermat')
    # generate_prime_nums(use_blum_blum_shub=True, use_miller_rabin=False)
    # print('\n\n\n\ngerar numeros aleatorio com o algoritmo xorshift e teste de miller rabin')
    # generate_prime_nums(use_blum_blum_shub=False, use_miller_rabin=True)
    # print('\n\n\n\ngerar numeros aleatorio com o algoritmo xorshift e teste de fermat')
    # generate_prime_nums(use_blum_blum_shub=False, use_miller_rabin=False)
