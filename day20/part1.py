modules = {}
lines = open(0).read().splitlines()
BRD = 'broadcaster'
conjunction_inputs = {}
for line in lines:
    module, targets = line.strip().split(' -> ')
    targets = targets.split(', ')
    if module == BRD:
        modules[BRD] = targets
    elif module[0] == '%':
        modules[module[1:]] = ['flipflop', False] + targets
    else:
        modules[module[1:]] = ['conjunction'] + targets
        conjunction_inputs[module[1:]] = {}

for line in lines:
    module, targets = line.strip().split(' -> ')
    if module[0] == '%':
        for t in targets.split(', '):
            if modules[t][0] == 'conjunction':
                conjunction_inputs[t][module[1:]] = 'low'
    elif module[0] == '&':
        for t in targets.split(', '):
            if t in modules and modules[t][0] == 'conjunction':
                conjunction_inputs[t][module[1:]] = 'low'

n = 1000
nb_low, nb_high = 0, 0
for _ in range(n):
    queue = [('button', BRD, 'low')]
    while queue:
        source, target, pulse = queue.pop(0)
        # print(source + " -" + pulse + "-> " + target)
        nb_low += (pulse == 'low')
        nb_high += (pulse == 'high')
        if target not in modules:
            continue
        if target == BRD:
            for t in modules[BRD]:
                queue.append((BRD, t, pulse))
        else:
            target_type = modules[target][0]
            if target_type == 'flipflop' and pulse == 'low':
                pulse_to_send = 'low' if modules[target][1] else 'high'
                modules[target][1] = not modules[target][1]
                for t in modules[target][2:]:
                    queue.append((target, t, pulse_to_send))
            elif target_type == 'conjunction':
                conjunction_inputs[target][source] = pulse
                pulse_to_send = 'low'
                for p in conjunction_inputs[target]:
                    if conjunction_inputs[target][p] == 'low':
                        pulse_to_send = 'high'
                        break
                for t in modules[target][1:]:
                    queue.append((target, t, pulse_to_send))

print(nb_low * nb_high)