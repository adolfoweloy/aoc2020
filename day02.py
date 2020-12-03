import sys
from typing import List
from typing import Tuple


class Passwords:
    # returns how many passwords are valid for a given list of policies/passwords
    def solve(self, elements: List[Tuple[int, int, str, str]]) -> int:
        total = 0
        for e in elements:
            if self.valid_password_part_two(range(e[0], e[1]), e[2], e[3]):
                total = total + 1
        return total

    def valid_password(self, policy: range, char: str, password: str) -> bool:
        count = password.count(char)
        policy.stop = policy.stop + 1
        if count in policy:
            return True
        else:
            return False

    def valid_password_part_two(self, policy: range, char: str, password: str) -> bool:
        if not (policy.start < len(password) >= policy.stop):
            return False
        position1 = policy.start - 1
        position2 = policy.stop - 1
        v1 = 1 if password[position1] == char else 0
        v2 = 1 if password[position2] == char else 0
        return (v1 + v2) == 1


if __name__ == '__main__':
    path = sys.argv[1]
    file_handle = open(path, 'r')

    entries: List[Tuple[int, int, str, str]] = []

    line = file_handle.readline()
    while line:
        entry = line.split()
        range_list = [int(x) for x in entry[0].split("-")]
        character = entry[1][:1]
        password = entry[2]
        entries.append((range_list[0], range_list[1], character, password))
        line = file_handle.readline()

    passwords = Passwords()
    res = passwords.solve(entries)

    print(res)
