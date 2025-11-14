# LCG parameters (using values from C++11's min_rand)
MODULUS = 2**31 - 1
MULTIPLIER = 48271
INCREMENT = 0

def generate_unique_random_numbers(seed, count):
    """
    Generates a list of unique pseudo-random numbers using a simple
    Linear Congruential Generator (LCG) without a class.
    """
    unique_numbers = []
    current_seed = seed
    while len(unique_numbers) < count:
        # Calculate the next number in the sequence
        current_seed = (MULTIPLIER * current_seed + INCREMENT) % MODULUS

        # Ensure the number is unique before adding it
        if current_seed not in unique_numbers:
            unique_numbers.append(current_seed)

    return unique_numbers

if __name__ == "__main__":
    # Use a fixed seed for reproducible results.
    initial_seed = 12345
    number_count = 10

    random_numbers = generate_unique_random_numbers(initial_seed, number_count)

    print("Generated 10 unique pseudo-random numbers:")
    print(random_numbers)
