# part 1
from itertools import tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

filename = "./input.txt"

# count = 0
with open(filename, "rt") as f:
    data = f.read().split()
    data = [int(x) for x in data]
pairs = pairwise(data)
increases = [x for x in pairs if x[0] < x[1]]
# print(len(increases)) # 1832


# part 2
from collections import deque

initial_window_1 = data[0:3]
initial_window_2 = data[1:4]

window1 = deque(initial_window_1, maxlen=3)
window2 = deque(initial_window_2, maxlen=3)

print(data[0:10])
print(window1)
print(window2)

count = 0
for height in data[3:]:

    if sum(window1) < sum(window2):
        count += 1
    window1 = window2.copy()
    window2.append(height)   

print(count)




