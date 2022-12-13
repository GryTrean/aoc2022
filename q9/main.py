class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"{self.x}-{self.y}"

    def adjacent(self, target):
        return abs(target.x - self.x) <= 1 and abs(target.y - self.y) <= 1

class Player:
    def __init__(self):
        self.visited = [[0, 0]]
        self.pos = Position()

    def move(self, move):
        if move == "R":
            self.pos.x += 1
        elif move == "L":
            self.pos.x -= 1
        elif move == "U":
            self.pos.y += 1
        elif move == "D":
            self.pos.y -= 1

    def moveTowards(self, target): #Target is a Player object
        if not self.pos.adjacent(target.pos):
            if target.pos.x == self.pos.x + 2 and target.pos.y == self.pos.y:
                self.move("R")
            elif target.pos.x == self.pos.x - 2 and target.pos.y == self.pos.y:
                self.move("L")
            elif target.pos.y == self.pos.y + 2 and target.pos.x == self.pos.x:
                self.move("U")
            elif target.pos.y == self.pos.y - 2 and target.pos.x == self.pos.x:
                self.move("D")
            else:
                if target.pos.x > self.pos.x:
                    self.move("R")
                elif target.pos.x < self.pos.x:
                    self.move("L")

                if target.pos.y > self.pos.y:
                    self.move("U")
                elif target.pos.y < self.pos.y:
                    self.move("D")

            self.visited.append([self.pos.x, self.pos.y])

head = Player()
tail = Player()

with open("input.txt") as f:
    moves = [[l.rstrip().split(" ")[0], int(l.rstrip().split(" ")[1])] for l in f.readlines()]
    for move in moves:
        for _ in range(move[1]):
            head.move(move[0])
            tail.moveTowards(head)

print(f"Part one: {len(set(map(tuple, tail.visited)))}")

#Part two
snake = [Player() for _ in range(10)] #snake[0] is the head, snake[1] is the tail
with open("input.txt") as f:
    moves = [[l.rstrip().split(" ")[0], int(l.rstrip().split(" ")[1])] for l in f.readlines()]

    for move in moves:
        for _ in range(move[1]):
            snake[0].move(move[0])
            for i in range(1, len(snake)):
                snake[i].moveTowards(snake[i-1])

print(f"Part two: {len(set(map(tuple, snake[-1].visited)))}")
