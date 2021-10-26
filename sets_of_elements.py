number_in_n_set, number_in_m_set = [int(x) for x in input().split()]

n_set = set()
m_set = set()

for _ in range(number_in_n_set):
    n_set.add(input())

for _ in range(number_in_m_set):
    m_set.add(input())

n_set.intersection_update(n_set, m_set)

for num in n_set:
    print(num)
