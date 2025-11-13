# LCG parameters (using values from C++11's min_rand)
MODULUS = 2**31 - 1
MULTIPLIER = 48271
INCREMENT = 0

class LCG:
    """A simple Linear Congruential Generator."""
    def __init__(self, seed):
        self.state = seed

    def next(self):
        """Generates the next pseudo-random number."""
        self.state = (MULTIPLIER * self.state + INCREMENT) % MODULUS
        return self.state

def generate_unique_random_numbers(seed, count):
    """Generates a list of unique pseudo-random numbers."""
    generator = LCG(seed)
    unique_numbers = []
    while len(unique_numbers) < count:
        num = generator.next()
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

if __name__ == "__main__":
    # For demonstration, we use a fixed seed. A common practice for
    # generating a "more random" seed is to use the current time,
    # but that would require importing a module like `time`.
    initial_seed = 12345
    number_count = 10

    random_numbers = generate_unique_random_numbers(initial_seed, number_count)

    print("Generated 10 unique pseudo-random numbers:")
    print(random_numbers)
