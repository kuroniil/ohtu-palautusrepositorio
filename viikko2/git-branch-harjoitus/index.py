# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
<<<<<<< HEAD
print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} + {y} = {erotus(x, y)}")
=======
print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} - {y} = {erotus(x, y)}")
>>>>>>> main

logger("lopetetaan")
print("goodbye!")
