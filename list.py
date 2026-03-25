list1 = [1,2,3,4,5]

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
# print(list1[5]) error!

list1[0] = 10

print(list1[0])

list1.append(6)
print(list1)

list2 = list1 + [7]
print(list2)

n=10
if n in list1:
    print('{}가 리스트에 있다.' .format(n))

list2 = [10, 20, 10, 30, 10, 40, 50]
print(list2)

del list2[-1]
print(list2)

list2.remove(10)
print(list2)