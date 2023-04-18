from number_generator import RandomNumberGenerator
from time import time

bits_amount = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
rng = RandomNumberGenerator()

print("Random Number Generator")
print("-----------------------")
print("Xorshift")
print()
for num_bits in bits_amount:
    begin = time()
    number = rng.xor_shift(num_bits)
    exec_time = (time() - begin)*1000

    print(f"Number generated: {number}")
    print(f"Bit amount: {num_bits}")
    print("Time elapsed: {:.4f}ms".format(exec_time))
    print()

print("-----------------------")
print("Linear Congruential Generator")
print()
for num_bits in bits_amount:
    begin = time()
    number = rng.lcg(num_bits)
    exec_time = (time() - begin)*1000

    print(f"Number generated: {number}")
    print(f"Bit amount: {num_bits}")
    print("Time elapsed: {:.4f}ms".format(exec_time))
    print()
