sequences = input().split(', ')
second_sequences = input().split(', ')

new_sequences = [sec for sec in sequences for sec_second in second_sequences if sec in sec_second]
new_sequences_list = []
# new_sequences_list = [x for x in new_sequences if x not in new_sequences_list]
for x in new_sequences:
    if x not in new_sequences_list:
        new_sequences_list.append(x)
print(new_sequences_list)
