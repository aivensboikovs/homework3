import random

# Check if a number is prime
def is_prime(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Miller-Rabin primality test
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    witness = [2, 3, 5, 7, 11, 13, 17]  # Witness values for Miller-Rabin test

    for a in witness:
        if pow(a, d, n) != 1:
            for r in range(s):
                if pow(a, d * 2**r, n) == n - 1:
                    break
            else:
                return False
    return True

# Generate random prime number
def generate_prime():
    while True:
        p = random.randint(2**15, 2**16)
        if is_prime(p):
            return p

# Generate public and private keys
def generate_keys():
    p = generate_prime()
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return p, g, y, x

# Encrypt a message
def encrypt(message, p, g, y):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = [(ord(char) * pow(y, k, p)) % p for char in message]
    return c1, c2

# Decrypt a message
def decrypt(c1, c2, p, x):
    decrypted_message = ''.join([chr((char * pow(c1, p - 1 - x, p)) % p) for char in c2])
    return decrypted_message

# Example usage
message = input("Enter the message to encrypt: ")

# Generate keys
p, g, y, x = generate_keys()

# Encrypt the message
c1, c2 = encrypt(message, p, g, y)

# Print generated keys
print("Generated Primitive Root (g):", g)
print("Generated Private Key (x):", x)

# Print the original message
print("Original message:", message)

# Decrypt the message
decrypted_message = decrypt(c1, c2, p, x)

# Print the decrypted message
print("Decrypted message:", decrypted_message)