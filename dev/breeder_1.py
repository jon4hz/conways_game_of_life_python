with open('breeder1.cells') as f:
    x = f.readlines()

arr = []
for i in x:
    tmp_arr = []
    if i[0] == '!':
        continue
    else:
        for j in i:
            if j == '.':
                tmp_arr.append(0)
            elif j == 'O':
                tmp_arr.append(1)
        while len(tmp_arr) != 749:
            tmp_arr.append(0)
        arr.append(tmp_arr)

print(len(arr))

with open('tmp.txt', 'w') as f:
    f.write('[\n')
    for i in arr:
        f.write('[')
        for j in i:
            f.write(f'{str(j)},')
        f.write('],\n')
    f.write('\n]')