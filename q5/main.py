schema = ''

with open('schema.txt') as f:
    data = [l.rstrip() for l in f.readlines()]
    COLS = int(data[-1][-1])
    ROWS = len(data) - 1

    schema = [[' ' for _ in range(ROWS)] for _ in range(COLS)]

    for i in range(COLS):
        for j in range(ROWS):
            if 1+4*i < len(data[j]):
                schema[i][j] = data[j][1+4*i]
            else:
                schema[i][j] = ' '

    schema = [[item for item in el if item != " "] for el in schema]


with open('steps.txt') as f:
    #[count, origin, destination]
    steps = [l.rstrip().replace("move ", "").replace("from ", "").replace("to ", "").split(" ") for l in f.readlines()]
    for step in steps:
        count = int(step[0])
        origin = int(step[1]) - 1
        destination = int(step[2]) - 1

        for i in range(count):
            no = schema[origin].pop(0)
            schema[destination].insert(0, no)


print(f"Answer: {''.join([c[0] for c in schema])}")


# PART TWO

schema = ''

with open('schema.txt') as f:
    data = [l.rstrip() for l in f.readlines()]
    COLS = int(data[-1][-1])
    ROWS = len(data) - 1

    schema = [[' ' for _ in range(ROWS)] for _ in range(COLS)]

    for i in range(COLS):
        for j in range(ROWS):
            if 1+4*i < len(data[j]):
                schema[i][j] = data[j][1+4*i]
            else:
                schema[i][j] = ' '

    schema = [[item for item in el if item != " "] for el in schema]


with open('steps.txt') as f:
    #[count, origin, destination]
    steps = [l.rstrip().replace("move ", "").replace(
        "from ", "").replace("to ", "").split(" ") for l in f.readlines()]

    for step in steps:
        count = int(step[0])
        origin = int(step[1]) - 1
        destination = int(step[2]) - 1

        print(f"Move {count} from {origin} to {destination}")

        items = schema[origin][0:count].copy()
        del schema[origin][0:count]

        for i in range(len(items) -1, -1, -1):
            schema[destination].insert(0, items[i])

    print(schema)


print(f"Answer: {''.join([c[0] for c in schema])}")
