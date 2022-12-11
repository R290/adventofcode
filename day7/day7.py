current_folder = ['/']
folder_list = {'/': []}
folder_size = {'/': 0} # size of files in folder without subfolders
path = '/'

with open('input', 'r') as f:

    for line in f.readlines():
        line = line.rstrip('\n')

        parts = line.split(' ')

        if parts[1] == 'cd':

            # move up
            if parts[2] == '..':
                current_folder.pop()
            elif parts[2] != '/':
                current_folder.append(parts[2])
                
                path = '/' + '/'.join(current_folder[1:])
                folder_list[path] = []
                folder_size[path] = 0

        elif parts[0] == 'dir':
            
            folder_list[path].append(path.rstrip('/') + '/' + parts[1])

        elif line[0].isdigit():
            
            folder_size[path] += int(parts[0])

folder_total_size = {}

while len(folder_size) != len(folder_total_size):

    for folder in folder_size:

        # no subfolders of unknown size
        if folder_list[folder] == []:
            folder_total_size[folder] = folder_size[folder]
        else:
            for f in folder_list[folder]:
                if f in folder_total_size:
                    folder_size[folder] += folder_total_size[f]
                    folder_list[folder].remove(f)


# 1
folder_sum = 0

for size in folder_total_size.values():
    if size <= 100000:
        folder_sum += size

print(folder_sum)

# 2
free_space = 70000000 - folder_total_size['/']
missing_free_space = 30000000 - free_space
folder_to_delete = '/'

for folder, size in folder_total_size.items():
    if size > missing_free_space:
        if size < folder_total_size[folder_to_delete]:
            folder_to_delete = folder

print(folder_total_size[folder_to_delete])