with open('input.txt') as f:
    data = [[l.rstrip()[0:len(l.rstrip())//2], l.rstrip()[len(l.rstrip())//2:]] for l in f.readlines()]
    priority = 0
    for l in data:
        dup = list(set(l[0]) & set(l[1]))[0]
        priority += ord(dup) - 38 if ord(dup) <= 91 else ord(dup) - 96

    print(f"Part one: {priority}")


with open('input.txt') as f:
    #PART TWO
    data = [l.rstrip() for l in f.readlines()]
    priorities = 0
    for i in range(0, len(data), 3):
        dup = list(set(data[i]) & set(data[i+1]) & set(data[i+2]))[0]
        priorities += ord(dup) - 38 if ord(dup) <= 91 else ord(dup) - 96

    print(f"Part two: {priorities}")