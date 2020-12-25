def game(cups, rounds, start):
    cups_min = min(cups.keys())
    cups_max = max(cups.keys())

    current = start
    for _ in range(rounds):
        pickup = []
        remove = current
        for _ in range(3):
            remove = cups[remove]
            pickup.append(remove)

        cups[current] = cups[remove]

        destination = current - 1
        if destination < cups_min:
            destination = cups_max
        if destination in pickup:
            while True:
                destination -= 1
                if destination < cups_min:
                    destination = cups_max
                if destination not in pickup:
                    break

        current_adjacent = cups[destination]
        cups[destination] = pickup[0]
        cups[pickup[0]] = pickup[1]
        cups[pickup[1]] = pickup[2]
        cups[pickup[2]] = current_adjacent

        current = cups[current]

    return cups


# input
with open('input.txt') as f:
    start = [int(x) for x in f.read().strip()]

# part 1
cups = {}
for index, cup in enumerate(start[:-1]):
    cups[cup] = start[index + 1]
cups[start[-1]] = start[0]
game1 = game(cups.copy(), 100, start[0])

ans1 = []
cup = 1
while True:
    cup = game1[cup]
    if cup != 1:
        ans1.append(str(cup))
    else:
        break
ans1 = ''.join(ans1)

# part 2
cups[start[-1]] = max(cups) + 1
for i in range(max(cups) + 1, 10**6):
    cups[i] = i+1
cups[10**6] = start[0]

game2 = game(cups.copy(), 10*10**6, start[0])
ans2 = game2[1] * game2[game2[1]]

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
