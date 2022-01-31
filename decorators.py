from operator import itemgetter


def person_lister(f):
    def inner(people):
        for x in people:
            x[2] = int(x[2])
        people = sorted(people, key=itemgetter(2))
        new_people = []
        for mans in people:
            new_people.append(f(mans))
        return new_people
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# matrix = []
# rols = int(input())
# for man in range(rols):
#     line = input().split()
#     matrix.append(line)
# sorted_matrix = sorted(matrix, key=itemgetter(2))
# print(matrix)
# 5
# Laura Moser 50 F
# Ted Moser 50 M
# Yena Dixit 50 F
# Diya Mirza 50 F
# Rex Dsouza 51 M
