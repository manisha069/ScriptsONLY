'''
Uses Miller-Rabin Primality Test
'''

WITNESSES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]

def testPrime(number: int, rand: bool = False, witnesses: list = WITNESSES) -> bool:
    """
    For better results, use more witnesses
    Random ones may slow down performance but are more reliable
    """
    if number < 2:
        return False
    if number == 2:
        return True

    if number < 1000:
        witnesses = [2]  # it should be good enough
    else:
        witnesses = witnesses

    if rand:
        import random

        witnesses += [random.randint(2, number - 3) for _ in range(10)]

    exp = 0
    mul = number - 1
    while mul % 2 == 0:
        mul >>= 1
        exp += 1
    for witness in witnesses:
        a = pow(witness, mul, number)
        if a == 1 or a == (number - 1):
            continue
        for _ in range(exp):
            a = pow(a, 2, number)
            if a == (number - 1):
                break
        else:
            return False
    return True


if __name__ == "__main__":
    for i in range(100):
        if testPrime(i):
            print(i)
    if testPrime(104717):
        print("prime!")
    if testPrime(282287659191997895566921940118430530569):
        print("prime!")
