"""

Projekt_2.py: Druhý projekt do Engeto Online Python Akadeie

author: Jiří Mlčkovský
email: jirkamlc@seznam.cz
discord:nemám založený profil na discordu
"""
import random

separe = '=' * 100

def pozdrav():
    print(separe)
    print("Hi there", separe, sep="\n")
    print("I've generated a random 4 digit number for you.Let's play a bulls and cows game.")
    print(separe)
    return()


ran_number = []

def computer_number():
    # Necháme počítač vygenerovat náhodné číslo
    while len(ran_number) != 4:
        ran_number.append(random.randrange(0, 10))
        if len(ran_number) == 4 and len(set(ran_number)) < 4:
            ran_number.clear()

    return()


pokusy = 0
zbyvajici_pokusy = 20
bulls = 0
cows = 0


def main():
    global pokusy, zbyvajici_pokusy, bulls, cows

    # Pravidlo pokračování/ukončení hry
    while bulls != 4 and zbyvajici_pokusy > 0:


        user_input = input('Enter a number: ')
        tip_user = [int(num) for num in str(user_input)]
        pokusy += 1
        zbyvajici_pokusy -= 1


        if len(tip_user) != 4:
            print('Enter 4 digit number! ')
            print(separe)
            continue


        for index, value in enumerate(tip_user):
            for pozice, hodnota in enumerate(ran_number):
                if index == pozice and value == hodnota:
                    bulls += 1

                elif index != pozice and value == hodnota:
                    cows += 1

        print(f'Bulls: {bulls}')
        print(f'Cows: {cows}')
        print(f'Zbývající pokusy: {zbyvajici_pokusy}')
        print(separe)


        if zbyvajici_pokusy == 0:
            print('End game.')

        elif bulls != 4:
            bulls = 0
            cows = 0

        else:
            bulls = 4
            cows = 0

            if pokusy < 11:
                print(f"'Correct, you've guessed the right number in 4 guesses! {pokusy}'")
            elif pokusy >= 11 and pokusy < 20:
                print(f"You won, next time can be better. Total number of {pokusy}'")


pozdrav()
computer_number()
main()

