import random
N = 10
values_1 = [random.randint(0,100) for a in range (N)]
print (values_1)
values_2 = [random.randint(0,100) for a in range (N)]
print (values_2)
values_3 = [random.randint(0,100) for a in range (N)]
print(values_3)

print("max:", max(max(values_1), max(values_2), max(values_3)))
print("sum: ", sum(values_1)+sum(values_2)+sum(values_3))