pool_v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
p1_total = p1 * h
p2_total = p2 * h
total_p1_and_p2 = p1_total + p2_total
total_v = 0
pipe_1 = 0
pipe_2 = 0
if pool_v >= total_p1_and_p2:
    total_v = total_p1_and_p2 * 100 / pool_v
    pipe_1 = p1_total * 100 / total_p1_and_p2
    pipe_2 = p2_total * 100 / total_p1_and_p2
    print(f'The pool is {total_v}% full. Pipe 1: {pipe_1}%. Pipe 2: {pipe_2}%.')
else:
    total_v = total_p1_and_p2 - pool_v
    print(f'For {h} hours the pool overflows with {total_v} liters.')
