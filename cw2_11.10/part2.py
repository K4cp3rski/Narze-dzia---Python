# Author: Kacper Cybiński
# Date: 11.10.2021
import sys
import math
import random as rnd


def print_out():
    for i in range(1, 4, 1):
        print(f"{i}: ", sys.argv[i])


def factorization():
    nr = int(input("Enter number to factorize: "))
    i = 2
    factors = []
    while i <= nr:
        if nr % i == 0:
            while nr % i == 0:
                nr = nr//i
                factors.append(i)
        i += 1
    print(factors)


def monte_carlo():
    it = int(input("How many interations?\n"))
    # it = 500000
    disp = int(input("How often show the partial result?\n"))
    # disp = 10000
    i = 0
    count = 0
    while i < it:
        x = rnd.random()
        y = rnd.random()
        pi = 4 * count / it
        if x**2 + y**2 < 1:
            count += 1
        if i % disp == 0:
            print(f"{i}: {pi}")
        i += 1
    # print(count)
    print("math.pi = {}\n".format(math.pi))
    print("nasze pi = {}\n".format(pi))
    rel_err = abs(100 - math.pi / pi * 100)
    print("Błąd procentowy to {:5f} %".format(rel_err))


if __name__ == "__main__":
    # print_out()
    monte_carlo()
    # factorization()
    print("Hello World!")
