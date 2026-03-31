for i in range(5): # == [0,1,2,3,4]
    print(i)

names = ['철수', '영희', '영수']
for i in range(len(names)):
    name = names[i]
    print('{}번: {}'.format(i + 1, name))

for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))