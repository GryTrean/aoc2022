queue = []
xreg = 1
cycle = 1

total = 0

def cycleCheck(c):
    global xreg, total, pic
    if c % 40 == 20:
        # print(f"Cycle {c}. Register: {xreg}. Signal strength {c * xreg}")
        total += c * xreg

    draw = "\n" if c % 40 == 1 else ""
    draw += "#" if abs(xreg - (c-1)%40) <= 1 else '.'

    # print(f"Cycle: {c}. Drawing in: {c-1} Xreg: {xreg}. Drawing: {'#' if abs(xreg - c%41 + 1) <= 1 else '.'}")

    print(draw, end="")

with open('input.txt') as f:
    lines = [l.rstrip() for l in f.readlines()]

    cycleCheck(cycle)

    for l in lines:
        cmd = l[0:4]

        if cmd == "addx":
            cycle += 1
            cycleCheck(cycle)

            xreg += int(l.split(" ")[1])

            cycle += 1
            cycleCheck(cycle)
        elif cmd == "noop":
            cycle += 1
            cycleCheck(cycle)

print(total)