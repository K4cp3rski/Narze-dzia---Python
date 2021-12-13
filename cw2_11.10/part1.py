# Author: Kacper Cybiński
# Date: 11.10.2021
import math

def startup():
    print("Hello, this is a startup program, please state your name:")
    a = input("")
    print("Hello {}, nice to see you".format(a))

def quadratic():
    print("Quadratic equation solver v1.0\nWe assume here quadratic equation given by: ax^2 + bx + c")
    a = float(input("Please enter coefficient 'a'\n"))
    b = float(input("Please enter coefficient 'a'\n"))
    c = float(input("Please enter coefficient 'a'\n"))
    delta = b**2 - 4*a*c
    print("Delta to: {:.1f}".format(delta))
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Miejsca zerowe to: {:.2f} i {:.2f}.".format(x1, x2))
    elif delta == 0:
        x0 = (-b) / (2 * a)
        print("Miejsce zerowe to: {:.2f}.".format(x0))
    else:
        print("Funkcja kwadratowa nie ma pierwiastków w ciele R")


def add(ingredient, price, balance):

    return balance


def pizza():
    print("Hello, what do you want on your pizza?\n")
    balance = 8.0
    ingredients = []
    ingredient1 = "pineapple"
    price1 = 2.0
    a1 = input("Do you want a {} on your pizza? (y/n)\n".format(ingredient1))
    if a1 == "y":
        balance += price1
        ingredients.append(ingredient1)
        print("{} added".format(ingredient1))
    else:
        print("{} not added".format(ingredient1))

    ingredient2 = "sausage"
    price2 = 4.0
    a2 = input("Do you want a {} on your pizza? (y/n)\n".format(ingredient2))
    if a2 == "y":
        balance += price2
        ingredients.append(ingredient2)
        print("{} added".format(ingredient2))
    else:
        print("{} not added".format(ingredient2))

    ingredient3 = "corn"
    price3 = 3.0
    a3 = input("Do you want a {} on your pizza? (y/n)\n".format(ingredient3))
    if a3 == "y":
        balance += price3
        ingredients.append(ingredient3)
        print("{} added".format(ingredient3))
    else:
        print("{} not added".format(ingredient3))

    ingredient4 = "olives"
    price4 = 5.0
    a4 = input("Do you want a {} on your pizza? (y/n)\n".format(ingredient4))
    if a4 == "y":
        balance += price4
        ingredients.append(ingredient4)
        print("{} added".format(ingredient4))
    else:
        print("{} not added".format(ingredient4))

    print("\nYou have ordered pizza with {}.".format(", ".join(ingredients), sep=","), "The price is ${}.".format(balance))
