import numpy as np
import re
from utils import read_file


def parse_line(line):
    m = re.search(r'#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)', line)
    if m:
        return {
            'id': int(m.group(1)),
            'x': int(m.group(2)),
            'y': int(m.group(3)),
            'width': int(m.group(4)),
            'height': int(m.group(5))
        }


print("#--- part1 ---#")
claims = []
for line in read_file('03.txt'):
    claims.append(parse_line(line))

max_x, max_y = 0, 0
for claim in claims:
    if claim['x'] + claim['width'] > max_x:
        max_x = claim['x'] + claim['width']
    if claim['y'] + claim['height'] > max_y:
        max_y = claim['y'] + claim['height']

cloth = np.zeros((max_x, max_y), dtype=np.int)
for claim in claims:
    for y in range(claim['y'], claim['y'] + claim['height']):
        for x in range(claim['x'], claim['x'] + claim['width']):
            cloth[x, y] += 1
print(len(np.argwhere(cloth > 1)))


print("#--- part2 ---#")
for claim in claims:
    nok = 0

    for y in range(claim['y'], claim['y'] + claim['height']):
        for x in range(claim['x'], claim['x'] + claim['width']):
            if cloth[x, y] != 1:
                nok += 1
    if nok == 0:
        print(claim['id'])
        quit()
