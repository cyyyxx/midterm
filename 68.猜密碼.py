n1 = input("請輸入第一組數字：")
n2= input("請輸入第二組數字：")
a, b = 0, 0
for i in n1:
    if i in n2:
        if n1.index(i) == n2.index(i):
            a += 1
        else:
            b += 1

print(f"{a}A{b}B",end=" 全對" if a == len(n1) else " 加油")