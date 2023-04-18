from prime_generator import PrimeGenerator
from time import time
from subprocess import Popen, PIPE

bits_amount = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
prime_rng = PrimeGenerator()

print("Prime Number Generator")
print("----------------------")
print("Xorshift + Fermat primality test")
print()
for num_bits in bits_amount:
    begin = time()
    number = prime_rng.xor_shift_fermat(num_bits)
    time_elapsed = (time() - begin)*1000

    cmd = f"openssl prime {number}"
    openssl_result = Popen(cmd, stdout=PIPE, shell=True).stdout.read().decode('utf-8')
    if "not" in openssl_result:
        openssl_result = "not a prime"
    else:
        openssl_result = "prime"

    print(f"Number generated: {number}")
    print(f"Bit amount: {num_bits}")
    print("Time elapsed: {:.4f}ms".format(time_elapsed))
    print(f"OpenSSL result: {openssl_result}")
    print()

print("----------------------")
print("Xorshift + Miller-rabin")
print()
for num_bits in bits_amount:
    begin = time()
    number = prime_rng.xor_shift_miller_rabin(num_bits)
    time_elapsed = (time() - begin)*1000

    cmd = f"openssl prime {number}"
    openssl_result = Popen(cmd, stdout=PIPE, shell=True).stdout.read().decode('utf-8')
    if "not" in openssl_result:
        openssl_result = "not a prime"
    else:
        openssl_result = "prime"

    print(f"Number generated: {number}")
    print(f"Bit amount: {num_bits}")
    print("Time elapsed: {:.4f}ms".format(time_elapsed))
    print(f"OpenSSL result: {openssl_result}")
    print()

print("----------------------")
print("Xorshift + Miller-rabin and Fermat primality test")
print()
for num_bits in bits_amount:
    begin = time()
    number = prime_rng.xor_shift(num_bits)
    time_elapsed = (time() - begin)*1000

    cmd = f"openssl prime {number}"
    openssl_result = Popen(cmd, stdout=PIPE, shell=True).stdout.read().decode('utf-8')
    if "not" in openssl_result:
        openssl_result = "not a prime"
    else:
        openssl_result = "prime"

    print(f"Number generated: {number}")
    print(f"Bit amount: {num_bits}")
    print("Time elapsed: {:.4f}ms".format(time_elapsed))
    print(f"OpenSSL result: {openssl_result}")
    print()

print("----------------------")
print("Linear Congruential Generator + Fermat primality test")
print()
for num_bits in bits_amount:
    begin = time()
    number = prime_rng.lcg_fermat(num_bits)
    time_elapsed = (time() - begin)*1000

    cmd = f"openssl prime {number}"
    openssl_result = Popen(cmd, stdout=PIPE, shell=True).stdout.read().decode('utf-8')
    if "not" in openssl_result:
        openssl_result = "not a prime"
    else:
        openssl_result = "prime"

    print(f"Number generated: {number}")
    print(f"Bit amount: {num_bits}")
    print("Time elapsed: {:.4f}ms".format(time_elapsed))
    print(f"OpenSSL result: {openssl_result}")
    print()

print("----------------------")
print("Linear Congruential Generator + Miller-rabin")
print()
for num_bits in bits_amount:
    begin = time()
    number = prime_rng.lcg_miller_rabin(num_bits)
    time_elapsed = (time() - begin)*1000

    cmd = f"openssl prime {number}"
    openssl_result = Popen(cmd, stdout=PIPE, shell=True).stdout.read().decode('utf-8')
    if "not" in openssl_result:
        openssl_result = "not a prime"
    else:
        openssl_result = "prime"

    print(f"Number generated: {number}")
    print(f"Bit amount: {num_bits}")
    print("Time elapsed: {:.4f}ms".format(time_elapsed))
    print(f"OpenSSL result: {openssl_result}")
    print()

print("----------------------")
print("Linear Congruential Generator + Miller-rabin and Fermat primality test")
print()
for num_bits in bits_amount:
    begin = time()
    number = prime_rng.lcg(num_bits)
    time_elapsed = (time() - begin)*1000

    cmd = f"openssl prime {number}"
    openssl_result = Popen(cmd, stdout=PIPE, shell=True).stdout.read().decode('utf-8')
    if "not" in openssl_result:
        openssl_result = "not a prime"
    else:
        openssl_result = "prime"

    print(f"Number generated: {number}")
    print(f"Bit amount: {num_bits}")
    print("Time elapsed: {:.4f}ms".format(time_elapsed))
    print(f"OpenSSL result: {openssl_result}")
    print()
