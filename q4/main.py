with open('input.txt') as f:
    data = [[l.rstrip().split(',')[0].split('-'), l.rstrip().split(',')[1].split('-')] for l in f.readlines()]
    count = 0
    for row in data:
        if (int(row[0][0]) <= int(row[1][0]) and int(row[0][1]) >= int(row[1][1])) or (int(row[1][0]) <= int(row[0][0]) and int(row[1][1]) >= int(row[0][1])):
            count += 1

    print(f"Part one: {count}")

    #Part two
    count2 = 0
    for row in data:
        elf1 = [i for i in range(int(row[0][0]), int(row[0][1]) + 1)]
        elf2 = [i for i in range(int(row[1][0]), int(row[1][1]) + 1)]
        overlap = len(list(set(elf1) & set(elf2)))
        if overlap > 0:
            count2 += 1

    print(f"Part two: {count2}")
