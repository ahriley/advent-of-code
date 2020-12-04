import numpy as np

# read in data
id, x, y, w, h = [], [], [], [], []
with open('data/day3.txt') as f:
    for line in f:
        items = line.split()
        coord = items[2].split(',')
        shape = items[3].split('x')
        id.append(int(items[0][1:]))
        x.append(int(coord[0]))
        y.append(int(coord[1][:-1]))
        w.append(int(shape[0]))
        h.append(int(shape[1]))
x = np.array(x); y = np.array(y); w = np.array(w); h = np.array(h)

# board drawing function
def draw(blank, x, y, w, h):
    board = np.copy(blank)
    for i in range(x,x+w):
        for j in range(y,y+h):
            board[j][i] = 1
    return board

# part 1
blank = np.zeros((np.max(y)+np.max(h), np.max(x)+np.max(w)))
total = np.copy(blank)
for xi, yi, wi, hi in zip(x,y,w,h):
    total += draw(blank,xi,yi,wi,hi)
print(np.sum(total >=2))

# part 2
for idi, xi, yi, wi, hi in zip(id,x,y,w,h):
    board = draw(blank,xi,yi,wi,hi)
    if np.sum(total * board) == np.sum(board):
        answer = idi
        break
print(answer)
