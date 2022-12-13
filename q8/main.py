grid = []

with open('input.txt') as f:
    grid = [[int(x) for x in list(l.rstrip())] for l in f.readlines()]

visible = 0
for col in range(len(grid)):
    for row in range(len(grid[col])):
        if col == 0 or col == len(grid) - 1 or row == 0 or row == len(grid[col]) - 1:
            visible += 1
            continue
        else:
            size = grid[col][row]
            #Check row
            rowcheck = [False, False] #True if another tree obscures it
            for i in range(0, row):
                if grid[col][i] >= size:
                    rowcheck[0] = True
                    break

            for i in range(row + 1, len(grid[col])):
                if grid[col][i] >= size:
                    rowcheck[1] = True
                    break

            #Check col
            colcheck = [False, False]
            for i in range(0, col):
                if grid[i][row] >= size:
                    colcheck[0] = True
                    break

            for i in range(col + 1, len(grid)):
                if grid[i][row] >= size:
                    colcheck[1] = True
                    break


            if not rowcheck[0] or not rowcheck[1] or not colcheck[0] or not colcheck[1]:
                visible += 1
                # print(f"\n\nVisible: {col}-{row}. Size: {size}. Rowcheck: {rowcheck}. Colcheck: {colcheck}\n\n")

print(visible)

# PART TWO
distances = []
for col in range(len(grid)):
    for row in range(len(grid[col])):
        #Calculate the viewing score for tree at col, row
        views = [0, 0, 0, 0] #top, bottom, left, right
        size = grid[col][row]
        #Top
        for i in range(row - 1, -1, -1):
            if grid[col][i] < size:
                views[0] += 1
            else:
                views[0] += 1
                break

        #Bottom
        for i in range(row + 1, len(grid)):
            if grid[col][i] < size:
                views[1] += 1
            else:
                views[1] += 1
                break

        #Left
        for i in range(col - 1, -1, -1):
            if grid[i][row] < size:
                views[2] += 1
            else:
                views[2] += 1
                break

        #Right
        for i in range(col + 1, len(grid[col])):
            if grid[i][row] < size:
                views[3] += 1
            else:
                views[3] += 1
                break

        # print(f"Tree {col}-{row}. Scenic score: {views[0] * views[1] * views[2] * views[3]}. Views: {views}")
        distances.append(views[0] * views[1] * views[2] * views[3])

print(f"Part two: {max(distances)}")