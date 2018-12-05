import re
import numpy as np
from utils import read_file


print("#--- part1 ---#")
guard = None
sleep_timestamp = 0
sleep_times = np.zeros(10000, dtype=np.int)
guards = {}
for lines in sorted(read_file('04.txt')):
    m_guard = re.search(r'Guard #(\d+)', lines)
    m_asleep = re.search(r'(\d{2}):(\d{2}).*falls asleep', lines)
    m_wakes = re.search(r'(\d{2}):(\d{2}).*wakes up', lines)

    if m_guard:
        guard = int(m_guard.group(1))
    elif m_asleep:
        sleep_timestamp = int(m_asleep.group(1)) * 60 + int(m_asleep.group(2))
    elif m_wakes:
        wake_timestamp = int(m_wakes.group(1)) * 60 + int(m_wakes.group(2))
        if guard not in guards:
            guards[guard] = np.zeros(60, dtype=np.int)
        for i in range(sleep_timestamp, wake_timestamp):
            guards[guard][i] += 1
        sleep_times[guard] += wake_timestamp - sleep_timestamp
guard = np.argmax(sleep_times)
index = np.unravel_index(guards[guard].argmax(), guards[guard].shape)[0]
print(guard * index)


print("#--- part2 ---#")
max_ = 0
guard = 0
index = -1
for k, v in guards.items():
    if max(v) > max_:
        max_ = max(v)
        guard = k
        index = np.argmax(v)
print(guard * index)
