from collections import deque

fireworks_effects = deque([int(x) for x in input().split(', ')])
explosive_power = deque([int(x) for x in input().split(', ')])

palm_firework = 0
willow_firework = 0
crossette_firework = 0
is_successfully = False

while fireworks_effects and explosive_power:
    effects = fireworks_effects.popleft()
    explosive = explosive_power.pop()
    if effects <= 0:
        explosive_power.append(explosive)
        continue
    if explosive <= 0:
        fireworks_effects.appendleft(effects)
        continue
    if (effects + explosive) % 3 == 0 and not (effects + explosive) % 5 == 0:
        palm_firework += 1
    elif (effects + explosive) % 5 == 0 and not (effects + explosive) % 3 == 0:
        willow_firework += 1
    elif (effects + explosive) % 5 == 0 and (effects + explosive) % 3 == 0:
        crossette_firework += 1
    else:
        effects -= 1
        fireworks_effects.append(effects)
        explosive_power.append(explosive)
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        is_successfully = True
        break

if is_successfully:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")
