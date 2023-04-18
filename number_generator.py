from time import time

class RandomNumberGenerator:
    def __init__(self, seed = None):
        # If no seed is set, use current time
        if seed is None:
            seed = int(time())

        # Making sure our seed is a int
        self.seed = int(seed)

        # A modulus so the seed doesn't take a lot of space
        self.modulus = 2**32

    def xor_shift_generator(self):
        # Generates a random number doing a XOR with
        # the seed and the seed shifted a certain amount of bits
        self.seed ^= self.seed << 13
        self.seed ^= self.seed >> 17
        self.seed ^= self.seed << 5
        self.seed %= self.modulus
        
        return self.seed

    def xor_shift(self, num_bits, minimum = 0, maximum = None):
        ret = self.xor_shift_generator()

        # While return doesn't have the desired number of bits, keep
        # generating more numbers and concatenate them to it
        while ret.bit_length() < num_bits:
            gen = self.xor_shift_generator()
            n = gen.bit_length()
            ret = (ret << n) | gen

        # AND with a mask to make sure the return has maximum size of num_bits
        mask = 2**num_bits - 1
        ret &= mask

        # Makes sure the generated number is between min and max specified
        if maximum is not None:
            ret %= maximum - minimum
        ret += minimum

        return ret
        
    def lcg_generator(self):
        a = 1372383749
        c = 1289706101

        # Generates a random number with the formula
        # (a * seed) + c) % modulus
        self.seed = (a * self.seed + c) % self.modulus
        
        return self.seed
        
    def lcg(self, num_bits, minimum = 0, maximum = None):
        ret = self.lcg_generator()

        # While return doesn't have the desired number of bits, keep
        # generating more numbers and concatenate them to it
        while ret.bit_length() < num_bits:
            gen = self.lcg_generator()
            n = gen.bit_length()
            ret = (ret << n) | gen

        # AND with a mask to make sure the return has maximum size of num_bits
        mask = 2**num_bits - 1
        ret &= mask

        # Makes sure the generated number is between min and max specified
        if maximum is not None:
            ret %= maximum - minimum
        ret += minimum

        return ret
