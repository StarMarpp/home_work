import random

def coin_flip():
    coin_sides = ['Орел', 'Решка']
    return random.choice(coin_sides)

while True:
    try1 = coin_flip()
    try2 = coin_flip()
    try3 = coin_flip()
    if try1 == try2 and try2 == try3 and try1 == try3:
        break