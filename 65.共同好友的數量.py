same,ll = 0,0
a= input("請輸入A的好友:").split(" ")
b = input("請輸入B的好友:").split(" ")
if a > b:
    ll = len(b)
else:
    ll = len(a)
for i in range(ll):
    if a[i] in b:
        same += 1
print(same)