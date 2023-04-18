from number_generator import RandomNumberGenerator
from prime_verifier import PrimeVerifier

class PrimeGenerator:
    def __init__(self, seed = None):
        self.rng = RandomNumberGenerator(seed)

    def __xor_shift_odd(self, num_bits):
        ret = self.rng.xor_shift(num_bits)

        # If number is even, turn it odd
        if ret % 2 == 0:
            ret += 1

        return ret

    def __lcg_odd(self, num_bits):
        ret = self.rng.lcg(num_bits)

        # If number is even, turn it odd
        if ret % 2 == 0:
            ret += 1

        return ret

    def xor_shift_fermat(self, num_bits, verifier_attempts = 20):
        ret = 0

        # Keep generating random numbers until it generates a prime
        while True:
            ret = self.__xor_shift_odd(num_bits)

            if PrimeVerifier.fermat(ret, verifier_attempts):
                break

        return ret

    def lcg_fermat(self, num_bits, verifier_attempts = 20):
        ret = 0
        
        # Keep generating random numbers until it generates a prime
        while True:
            ret = self.__lcg_odd(num_bits)

            if PrimeVerifier.fermat(ret, verifier_attempts):
                break

        return ret


    def xor_shift_miller_rabin(self, num_bits, verifier_attempts = 20):
        ret = 0
        
        # Keep generating random numbers until it generates a prime
        while True:
            ret = self.__xor_shift_odd(num_bits)

            if PrimeVerifier.miller_rabin(ret, verifier_attempts):
                break

        return ret

    def lcg_miller_rabin(self, num_bits, verifier_attempts = 20):
        ret = 0
        
        # Keep generating random numbers until it generates a prime
        while True:
            ret = self.__lcg_odd(num_bits)

            if PrimeVerifier.miller_rabin(ret, verifier_attempts):
                break

        return ret

    def xor_shift(self, num_bits, verifier_attempts = 20):
        ret = 0
        
        # Keep generating random numbers until it generates a prime
        while True:
            ret = self.rng.xor_shift(num_bits)

            if PrimeVerifier.miller_rabin(ret, verifier_attempts) and PrimeVerifier.fermat(ret, verifier_attempts):
                break

        return ret

    def lcg(self, num_bits, verifier_attempts = 20):
        ret = 0
        
        # Keep generating random numbers until it generates a prime
        while True:
            ret = self.__lcg_odd(num_bits)

            if PrimeVerifier.miller_rabin(ret, verifier_attempts) and PrimeVerifier.fermat(ret, verifier_attempts):
                break

        return ret
