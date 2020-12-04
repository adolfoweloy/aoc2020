import sys
from typing import List, Dict
from re import search

RIGHT = 1
DOWN = -1


def validate(s: str, v: str) -> bool:
    if s == "byr":
        r = search("^(\\d{4})$", v)
        if r:
            byr = int(r.group(0))
            return byr in range(1920, 2003)

    if s == "iyr":
        r = search("^(\\d{4})$", v)
        if r:
            iyr = int(r.group(0))
            return iyr in range(2010, 2021)

    if s == "eyr":
        r = search("^(\\d{4})$", v)
        if r:
            eyr = int(r.group(0))
            return eyr in range(2020, 2031)

    if s == "hgt":
        r = search("^(\\d+)(cm|in)$", v)
        if r:
            height = int(r.group(1))
            unit = r.group(2)
            if unit == "cm":
                return height in range(150, 194)
            if unit == "in":
                return height in range(59, 77)

    if s == "hcl":
        r = search("^#[0-9a-f]{6}$", v)
        return True if r else False

    if s == "ecl":
        r = search("^amb|blu|brn|gry|grn|hzl|oth$", v)
        return True if r else False

    if s == "pid":
        r = search("^\\d{9}$", v)
        return True if r else False

    if s == "cid":
        return True
    return False


def get_fields() -> List[str]:
    return ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def get_key(x: List[str]) -> str:
    return x[0]


def valid_fields(x: Dict[str, str]) -> bool:
    for key in x:
        if not validate(key, x[key]):
            return False
    return True


if __name__ == '__main__':
    path = sys.argv[1]
    entries = []

    # prepare
    with open(path, 'r') as reader:
        for line in reader.readlines():
            cols = line.strip().split(" ")
            entries.append({y.split(":")[0]: y.split(":")[1] for y in cols})

    # algorithm
    valid_items = 0
    for entry in entries:
        fields = get_fields()
        if len(fields) == len(entry) or (len(fields) - 1 == len(entry) and "cid" not in entry):
            if valid_fields(entry):
                valid_items = valid_items + 1

    print(valid_items)
