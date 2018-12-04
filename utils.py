def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines
