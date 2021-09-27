numbers = int(input())

negative = []
positive = []
positive_counter = 0

for number in range(numbers):
    num = int(input())
    if num < 0:
        negative.append(num)
    else:
        positive_counter += 1
        positive.append(num)

print(f'{positive}\n{negative}')
print(f"Count of positives: {positive_counter}. Sum of negatives: {sum(negative)}")
