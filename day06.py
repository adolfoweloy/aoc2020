import sys
from typing import Set


def get_chars(e: str) -> Set[str]:
    r: Set[str] = set()
    for i in e:
        r.add(i)
    return r


if __name__ == '__main__':
    path = sys.argv[1]
    # answer 1
    with open(path, 'r') as reader:
        lines = reader.readlines()
        count = 0
        tmp: Set[str] = set()
        for line in lines:
            line = line.strip()
            if line:
                tmp = tmp.union(get_chars(line))
            else:
                count += len(tmp)
                tmp = set()
        if len(tmp) > 0:
            count += len(tmp)
        print(count)

    # answer 2
    with open(path, 'r') as reader:
        lines = reader.readlines()
        count = 0
        tmp: Set[str] = set()
        reset: bool = True  # using a flag :cone_of_shame
        for line in lines:
            line = line.strip()
            if line:
                answers = get_chars(line)
                tmp = answers if reset else tmp.intersection(answers)
                reset = False
            else:
                count = count + len(tmp)
                tmp = set()
                reset = True
        if len(tmp) > 0:
            count += len(tmp)
        print(count)
