from utils import read_file
from collections import defaultdict
import re


data = read_file('07.txt')
graph = defaultdict(set)
for line in data:
    m = re.search(r'Step (.).+before step (.)', line)
    if m:
        graph[m.group(1)].add(m.group(2))
        if m.group(2) not in graph:
            graph[m.group(2)] = set()


def part1(graph):
    print("#--- part1 ---#")
    result = ''
    while True:
        nodes = set(graph.keys())
        for _, v in graph.items():
            for child in v:
                if child in nodes:
                    nodes.remove(child)
        if len(nodes) < 1:
            break
        del graph[sorted(nodes)[0]]
        result += sorted(nodes)[0]
    print(result)


def part2(graph):
    print("#--- part2 ---#")
    print('')

part1(graph.copy())

