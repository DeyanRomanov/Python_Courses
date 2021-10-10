miner = input()

counter = 0
miner_list = []
miner_dict = {}

while not miner == 'stop':
    miner_list.append(miner)
    miner = input()

for miner in range(len(miner_list)):
    if miner % 2 == 0:
        key = miner_list[miner]
    else:
        if key in miner_dict:
            miner_dict[key] += int(miner_list[miner])
        else:
            miner_dict[key] = int(miner_list[miner])
for key, value in miner_dict.items():
    print(f'{key} -> {value}')