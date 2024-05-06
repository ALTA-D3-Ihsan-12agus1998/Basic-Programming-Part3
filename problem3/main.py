def prime_number(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return "Not Prime"
        return "Prime"
    else:
        return "Not Prime"

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"
