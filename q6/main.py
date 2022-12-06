with open('input.txt') as f:
    data = f.readline().rstrip()

    i = 3
    while i < len(data):
        if len(list(set(data[i-4:i]))) == 4:
            print(i)
            break

        i += 1

    #part two
    j = 13
    while j < len(data):
        if len(list(set(data[j-14:j]))) == 14:
            print(j)
            break

        j += 1
