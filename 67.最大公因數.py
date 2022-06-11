a = input().split(",")
same,time = 0,0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] != a[j]:
            if int(a[i]) < int(a[j]):
                time = int(a[i])
            else:
                time = int(a[j])
            for k in range(1,time+1):
                if int(a[i]) % k == 0 and int(a[j]) % k == 0 and k > same:
                    same = k
print(same)