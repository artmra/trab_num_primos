from blum_blum_shub import BlumBlumShub
from xorshift_1024_s import Xorshift1024s

BITS_TO_GENERATE = [40, 56, 80, 128, 168, 224, 256, 1024, 2048, 4096]

if __name__ == '__main__':
    blum_blum_shub = BlumBlumShub()
    for size in BITS_TO_GENERATE:
        print('Blum Blum Shub com ', size, 'bits: ', blum_blum_shub.generate(size))

    xorshift_1024_s = Xorshift1024s()
    for size in BITS_TO_GENERATE:
        print('Xorshift1024* com ', size, 'bits: ', xorshift_1024_s.generate(size))
