import random

def generate():
    return random.randint(1, 6)

def is_done(pos):
    return pos == 100

snakes = {22: 6, 45: 30, 96: 64}
ladders = {7: 24, 21: 77, 42: 90, 40: 60}

p1 = 1
p2 = 1

while True:
    p = int(input("Enter the player number "))

    if p == 1:
        num = generate()
        print("Player 1 rolled:", num)
        if p1 + num <= 100:
            p1 += num
            if p1 in snakes:
                print("Snake Go down", snakes[p1])
                p1 = snakes[p1]
            elif p1 in ladders:
                print("Ladder! Climb", ladders[p1])
                p1 = ladders[p1]
        print("Player 1 at:", p1)
        print("Player 2 at:", p2)
        if is_done(p1):
            print("Player 1 wins")
            break

    elif p == 2:
        num = generate()
        print("Player 2 rolled:", num)
        if p2 + num <= 100:
            p2 += num
            if p2 in snakes:
                print("Snake! Go down to", snakes[p2])
                p2 = snakes[p2]
            elif p2 in ladders:
                print("Ladder! Climb up to", ladders[p2])
                p2 = ladders[p2]
        print("Player 1 at:", p1)
        print("Player 2 at:", p2)
        if is_done(p2):
            print("Player 2 wins")
            break

    else:
        print("Enter only player 1 or 2")
