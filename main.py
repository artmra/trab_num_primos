from blum_blum_shub import BlumBlumShub
from xorshift_1024_s import Xorshift1024s

BITS_TO_GENERATE = [40, 56, 80, 128, 168, 224, 256, 1024, 2048, 4096]
NUMBER_OF_EXECUTIONS = 1


def generate_pseudo_random_nums(use_blum_blum_shub: bool = True) -> None:
    for size in BITS_TO_GENERATE:
        generator = BlumBlumShub() if use_blum_blum_shub else Xorshift1024s()
        average = 0
        for _ in range(NUMBER_OF_EXECUTIONS):
            _, execution_time = generator.generate(size)
            average += execution_time
        print('Tempo medio de execucao do algoritmo ', generator.get_algorithm_name(), ' para ', size, 'bits: ',
              average / 100)


if __name__ == '__main__':
    generate_pseudo_random_nums()
    generate_pseudo_random_nums(use_blum_blum_shub=False)
