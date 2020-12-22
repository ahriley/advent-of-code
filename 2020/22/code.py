# input
with open('input.txt') as f:
    player1, player2 = f.read().strip().split('\n\n')
    player1 = [int(x) for x in player1.split('\n')[1:]]
    player2 = [int(x) for x in player2.split('\n')[1:]]


def play_game(player1, player2, recurse=False):
    previous = set()
    while player1 and player2:
        state = (tuple(player1), tuple(player2))
        if state in previous:
            return (1, player1)
        previous.add(state)

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if not recurse:
            if card1 > card2:
                player1 += [card1, card2]
            else:
                player2 += [card2, card1]
        else:
            if len(player1) >= card1 and len(player2) >= card2:
                winner = play_game(player1[:card1], player2[:card2], True)
                if winner[0] == 1:
                    player1 += [card1, card2]
                else:
                    player2 += [card2, card1]
            else:
                if card1 > card2:
                    player1 += [card1, card2]
                else:
                    player2 += [card2, card1]
    return (1, player1) if player1 else (2, player2)


def score(winner):
    score = 0
    for scale, card in enumerate(winner[::-1]):
        score += (scale + 1) * card
    return score


# part 1 (without recursion)
ans1 = score(play_game(player1.copy(), player2.copy())[1])

# part 2 (with recursion)
ans2 = score(play_game(player1.copy(), player2.copy(), True)[1])

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
