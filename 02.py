from utils import read_file

print("#--- part1 ---#")
twos = 0
threes = 0
for id_ in read_file('02.txt'):
    result = {}
    for letter in list(id_):
        result[letter] = result.get(letter, 0) + 1
    s = set()
    for k, v in result.items():
        s.add(v)
    if 2 in s:
        twos += 1
    if 3 in s:
        threes += 1
print(twos * threes)


print("#--- part2 ---#")


def compare(str1, str2):
    diffs = 0
    common = ''
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diffs += 1
        else:
            common += str1[i]
    return diffs, common

ids = read_file('02.txt')
for a in range(len(ids)):
    for b in range(a + 1, len(ids)):
        diffs, common = compare(ids[a], ids[b])
        if diffs == 1:
            print(common)
            quit()
