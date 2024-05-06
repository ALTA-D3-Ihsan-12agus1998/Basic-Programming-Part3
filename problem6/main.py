def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def full_prima(N):
    if N < 0:
        return False
    N_str = str(N)
    for digit in N_str:
        if not is_prime(int(digit)):
            return False
    return True

if __name__ == '__main__':
    print(full_prima(2))  # True
    print(full_prima(3))  # True
    print(full_prima(11))  # False
    print(full_prima(13))  # False
    print(full_prima(23))  # True
    print(full_prima(29))  # False
    print(full_prima(37))  # True
    print(full_prima(41))  # False
    print(full_prima(43))  # False
    print(full_prima(53))  # True
