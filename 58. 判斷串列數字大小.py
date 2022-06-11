c = []
for i in range(10):
    a =int(input("輸入第{}個數字:".format(i+1)))
    c.append(a)
print(f'最大的3個數字為:{c[-3]},{c[-2]},{c[-1]}')
print(f'最小的3個數字為:{c[2]},{c[1]},{c[0]}')
