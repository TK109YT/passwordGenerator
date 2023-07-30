# It's simple but effective 

import random as rndm
import colorama
from colorama import Fore, init

init()

red = Fore.RED
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
yellow = Fore.YELLOW
white = Fore.WHITE


letrasNecesarias_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letrasNecesarias_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numerosNecesarios = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
caracteresEspecialesNecesarios = ["!", "#", ",", ";", ":"]

longitud = int(input(f"{red}¿Longitud de la contraseña? (Número de caracteres) --> {lgreen}\033[1m"))
necesario = letrasNecesarias_mayusculas + letrasNecesarias_minusculas + numerosNecesarios + caracteresEspecialesNecesarios
contraseña = f"\033[0m{red}La contraseña es: {green}\033[1m" + "".join(rndm.sample(necesario, longitud)) + "\033[0m"
print(contraseña)
    
