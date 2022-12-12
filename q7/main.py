filestructure = {
    "/": {}
}

#Each file is saved as [name, size]

curloc = '/'
lines = ''

with open('input.txt') as f:
    lines = [l.rstrip() for l in f.readlines()]


#Generate file structure
i = 0
while i < len(lines):
    parts = lines[i].split(" ")
    if parts[0] == "$":
        # User commands
        if parts[1] == "cd":
            # Changing directory
            if parts[2] == "/":
                curloc = '/'
            elif parts[2] == '..':
                curloc = "/".join(curloc.split("/")[:-1])
                if curloc == "":
                    curloc = "/"
            else:
                if curloc[-1] == "/":
                    curloc += parts[2]
                else:
                    curloc += "/" + parts[2]
        elif parts[1] == "ls":
            while lines[i+1][0] != "$":
                el = lines[i+1]
                elp = el.split(" ")

                locindicies = curloc.split("/")[1::]

                if locindicies[0] != "/" and locindicies[0] != "":
                    locindicies.insert(0, "/")

                varstring = "".join([f"{[ind if ind != '' else '/']}" for ind in locindicies])

                if elp[0] == "dir":
                    exec("filestructure" + varstring + "['" + elp[1] +"'] = {}")
                else:
                    exec("filestructure" + varstring + "['" + elp[1] + "'] = " + elp[0])

                i += 1
                if i+1 >= len(lines):
                    break

    i += 1

MAXSIZE = 100000

def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v

def DirSize(dir):
    return sum(NestedDictValues(dir))

part1 = 0

def CheckDir(dir):
    global part1
    size = DirSize(dir)
    if size <= MAXSIZE:
        part1 += size

    for el in dir.values():
        if isinstance(el, dict):
            CheckDir(el)


CheckDir(filestructure['/'])
print(f"Part 1: {part1}")

# PART TWO
DISKSIZE = 70_000_000
NEEDED_SPACE = 30_000_000
USED_SPACE = DirSize(filestructure)

UNUSED_SPACE = DISKSIZE - USED_SPACE

NEED_TO_DELETE = NEEDED_SPACE - UNUSED_SPACE

print(f"Need to delete: {NEED_TO_DELETE}")

possibilities = []

def FindDirectoriesMinSize(dir, minsize):
    global possibilities
    size = DirSize(dir)

    if size >= minsize:
        possibilities.append(size)

    for el in dir.values():
        if isinstance(el, dict):
            FindDirectoriesMinSize(el, minsize)

FindDirectoriesMinSize(filestructure["/"], NEED_TO_DELETE)
print(f"Part two: {min(possibilities)}")