a = int(input("請輸入正整數n:"))
num = []
total = 0
for i in range(1,a):
    if a % i == 0:
        num.append(i)
for i in num:
    total += i
if total > a:
    print("abundant")
elif total == a:
    print("perfect")
else:
    print("deficient")