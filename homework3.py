import random

def is_prime(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True


    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    witness = [2, 3, 5, 7, 11, 13, 17]

    for a in witness:
        if pow(a, d, n) != 1:
            for r in range(s):
                if pow(a, d * 2**r, n) == n - 1:
                    break
            else:
                return False
    return True

def generate_prime():
    while True:
        p = random.randint(2**15, 2**16)
        if is_prime(p):
            return p

def generate_keys():
    p = generate_prime()
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return p, g, y, x

def encrypt(message, p, g, y):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = [(ord(char) * pow(y, k, p)) % p for char in message]
    return c1, c2

def decrypt(c1, c2, p, x):
    decrypted_message = ''.join([chr((char * pow(c1, p - 1 - x, p)) % p) for char in c2])
    return decrypted_message

message = input("Enter the message to encrypt: ")

p, g, y, x = generate_keys()

c1, c2 = encrypt(message, p, g, y)

print("Generated Primitive Root (g):", g)
print("Generated Private Key (x):", x)

print("Original message:", message)

decrypted_message = decrypt(c1, c2, p, x)

print("Decrypted message:", decrypted_message)