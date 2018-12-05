from utils import read_file


pairs = []
for i in range(ord('A'), ord('Z') + 1):
    pairs.append("%c%c" % (i, i + 32))
    pairs.append("%c%c" % (i + 32, i))


def _reduce(chain):
    for pair in pairs:
        chain = chain.replace(pair, '')
    return chain


def reduce(chain):
    while True:
        chain_ = _reduce(chain)
        if len(chain) == len(chain_):
            break
        chain = chain_
    return chain_

print("#--- part1 ---#")
data = read_file('05.txt')[0]
data_ = reduce(data)
print(len(data_))


print("#--- part2 ---#")
data = read_file('05.txt')[0]
min_len = len(data)
for i in range(ord('A'), ord('Z') + 1):
    data_ = data.replace(chr(i), '').replace(chr(i + 32), '')
    if data == data_:
        next
    len_ = len(reduce(data_))
    if len_ < min_len:
        min_len = len_
print(min_len)
