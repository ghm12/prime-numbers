from number_generator import RandomNumberGenerator

class PrimeVerifier:
    @staticmethod
    def miller_rabin(n, attempts: int = 20):
        # n must be odd for this algorithm
        if n % 2 == 0:
            return False

        # obtaining the biggest d and s possible
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1

        rng = RandomNumberGenerator()
        a = 0
        for _ in range(attempts):
            # getting a base between 2 and n-2
            a = rng.xor_shift(n.bit_length(), 2, n-2)

            # x has both the value of a**d and a**((2**0)*d)
            # if x % n == 1 or x % n == -1 (n-1) then its probably prime,
            # keep trying other bases
            x = pow(a, d, n)
            if x == 1 or x == n-1:
                continue

            # failing the test above asks for the next test:
            # a ** ((2**r)*d) % n == -1 (n-1) for any 0 <= r < s
            # x has the value of (a ** d), so we just keep powering
            # it with 2s until r = s-1
            found = False
            for r in range(s):
                y = pow(x, 2, n)
                # if we found a 'r' value that a ** ((2**r)*d), then
                # we don't need to keep trying
                if y == n-1:
                    found = True
                    break
                x = y

            # if we found a 'r' value, its probably prime,
            # keep trying other bases
            if found:
                continue

            # if both tests failed, it's a composite number
            return False

        # if any of both tests succeeded for a lot of bases, it's probably a prime
        return True

    @staticmethod
    def fermat(n, attempts: int = 20):
        rng = RandomNumberGenerator()
        a = 0

        for _ in range(attempts):
            # getting a base between 0 and n-1
            a = rng.xor_shift(n.bit_length(), maximum=n-1)

            # according to fermat's primality test, for a random base 0 < a < n-1,
            # if a ** (n-1) % n != 1, then a is a fermat witness for the
            # compositeness of 'n'
            if pow(a, (n - 1), n) != 1:
                return False

        return True
 
