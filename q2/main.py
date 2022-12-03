#A (65) - Rock, B (66) - Paper, C (67) - Scissors
#X (88) - Rock, Y (89) - Paper, Z (90) - Scissors
#Diff = 23
p = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

#L = 0, D = 3, W = 6
scores = [3, 0, 6]
results = ["Z", "X", "Y", "Z", "X", "Y", "Z", "X", "Y"]

with open('input.txt') as f:
    data = [l.rstrip().split(" ") for l in f.readlines()]

    points = 0
    for l in data:
        points += scores[-(ord(l[1]) - 88) + ord(l[0]) - 65] + ord(l[1]) - 87

    print(f"Part one: {points}") #14531

    #PART TWO
    #X - need to lose, Y - need to draw, Z - need to win
    p2 = 0
    for l in data:
        #NY Y, O Z
        #          90 - (90        - 88) - (67        - 65)
        char = results[ord(l[0]) - 65 + (ord(l[1]) - 88)]
        # print(f"Need to {l[1]}. Opponent: {l[0]}. Selected: {char}")
        p2 += p[char] + (ord(l[1]) - 88) * 3

    print(f"Part two: {p2}")