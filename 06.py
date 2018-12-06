from utils import (
    read_file,
    manhattan_distance
)
import numpy as np


max_x, max_y = 0, 0
points = []
for row in read_file('06.txt'):
    x, y = row.split(", ")
    points.append((int(x), int(y)))
    if int(x) > max_x:
        max_x = int(x)
    if int(y) > max_y:
        max_y = int(y)


def part1():

    def closest_point(x, y, points):
        dist = 1000000000000
        point = -1
        for i in range(len(points)):
            dist_ = manhattan_distance((x, y), points[i])
            if dist_ < dist:
                dist = dist_
                point = i
            elif dist_ == dist:
                point = -1
        return point

    area = {}
    # genereate a grid of all the closes pont id:s
    grid = np.zeros((max_x + 1, max_y + 1), dtype=np.int)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            grid[x, y] = closest_point(x, y, points)
            area[grid[x, y]] = area.get(grid[x, y], 0) + 1

    # delete all border points
    for x in range(max_x + 1):
        area.pop(grid[x, 0], None)
        area.pop(grid[x, max_y], None)
    for y in range(max_y + 1):
        area.pop(grid[0, y], None)
        area.pop(grid[max_x, y], None)
    return max(area.values())


def part2():

    def sum_of_distances(x, y, points):
        dist = 0
        for point in points:
            dist += manhattan_distance((x, y), point)
        return dist

    grid = np.zeros((max_x + 1, max_y + 1), dtype=np.int)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            grid[x, y] = sum_of_distances(x, y, points)
    return len(np.argwhere(grid < 10000))


print("#--- part1 ---#")
print(part1())


print("#--- part2 ---#")
print(part2())
