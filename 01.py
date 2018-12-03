def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

print("#--- part1 ---#")
print(sum(map(int, read_file('01.txt'))))

print("#--- part2 ---#")
seen = set()
freq = 0
seen.add(freq)
done = False
while not done:
    for offset in map(int, read_file('01.txt')):
        freq += offset
        # print(freq)
        if freq in seen:
            print(freq)
            done = True
            break
        seen.add(freq)
