"""

Projekt_2.py: Druhý projekt do Engeto Online Python Akadeie

author: Jiří Mlčkovský
email: jirimlckovsky.obchod@post.cz
discord:nemám založený profil na discordu
"""

import random

separe = "=" * 100
while True:                             # vygenerování náhodného 4 místného čísla
    secret_number = random.randrange(1000, 10000)
    list_number = [int(s) for s in str(secret_number)]
    if sorted(list_number) == sorted(set(list_number)):
        break

#print("Your secret number is:", secret_number)
print("Hi there!")
print(separe)
print("I have generated a random 4 digit number for you.")
print(separe)
print("Enter a number: ")

counting = 0
while True:
    print(separe)
    user_try = (input()) #Uživatelský vstup
    if len(user_try) != 4 or not user_try.isdigit():     # číslo musí být 4 mítné
        print("Must be 4-digit ")
        continue
    if user_try[0] == "0":    # číslo nemuže začínat 0
        print("Cant start with 0")
        continue
    try_list = [int(s) for s in str(user_try)]
    if sorted(try_list) != sorted(set(try_list)):
        print("No duplicated digits")               # doplněno o duplicity
        continue
    counting += 1
    bull = 0
    cow = 0
    for i in range(4):
        if try_list[i] == list_number[i]:
            bull += 1
        elif try_list[i] in list_number:
            cow += 1
    if bull == 4:
        print(f"Correct, you've guessed the right number\nin {counting} guesses!")
        break
    else:
        bull_str = "bull" if bull == 1 else "bulls"
        cow_str = "cow" if cow == 1 else "cows"
        print(f"{bull} {bull_str}, {cow} {cow_str}")
print(separe)



