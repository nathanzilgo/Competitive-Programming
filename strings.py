from itertools import permutations

string_input = input()

perms = set([''.join(i) for i in permutations(string_input)])

print(len(perms))

for z in sorted(perms):
    print(z)