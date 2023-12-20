import utils

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
        if targets[0] == 'rx':
            rx_conj = module[1:]

rx_values = {}
for line in lines:
    module, targets = line.strip().split(' -> ')
    if rx_conj in targets:
        rx_values[module[1:]] = 0
    if module[0] == '%':
        for t in targets.split(', '):
            if modules[t][0] == 'conjunction':
                conjunction_inputs[t][module[1:]] = 'low'
    elif module[0] == '&':
        for t in targets.split(', '):
            if t in modules and modules[t][0] == 'conjunction':
                conjunction_inputs[t][module[1:]] = 'low'

n = 0
while True:
    queue = [('button', BRD, 'low')]
    n += 1
    while queue:
        source, target, pulse = queue.pop(0)
        if source in rx_values and rx_values[source] == 0 and pulse == 'high':
            rx_values[source] = n
            if all(x != 0 for x in list(rx_values.values())):
                print(utils.ppcm(list(rx_values.values())))
                quit()
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