with open('input.txt') as f:
    data = [l.rstrip() for l in f.readlines()]
    print(data)
    elfs = [0]

    i = 0
    for l in data:
        if l == '':
            i += 1
            continue

        if elfs[i]:
            elfs[i] += int(l)
        else:
            elfs.insert(i, int(l))

    print(f"Elf {elfs.index(max(elfs)) + 1} with {max(elfs)} cal")

    # PART TWO
    elfsSorted = sorted(elfs, reverse=True)
    print(f"The three top elves carry {elfsSorted[0] + elfsSorted[1] + elfsSorted[2]} cal")