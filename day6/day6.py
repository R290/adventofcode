with open('input', 'r') as f:
    orbit_list = f.readlines()

orbit_list = [s.strip() for s in orbit_list]

# part 1

orbit_map = {}

for orbit in orbit_list:

    object1,object2 = orbit.split(')')
    orbit_map[object2] = object1

orbit_counter = 0

for obj in orbit_map:
    
    while obj != 'COM':
        obj = orbit_map[obj]
        orbit_counter += 1

print('Part 1: {}'.format(orbit_counter))

# part 2

obj = 'YOU'
you_transfers = []

while obj != 'COM':
    obj = orbit_map[obj]
    you_transfers.append(obj)

obj = 'SAN'
transfer_counter = 0

while obj not in you_transfers:
    obj = orbit_map[obj]
    transfer_counter += 1

transfer_counter += you_transfers.index(obj) - 1

print('Part 2: {}'.format(transfer_counter))