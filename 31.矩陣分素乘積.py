col,row = input("輸入矩陣的維度:").split()
arr1,arr2 = [],[]
for i in range(int(col)):
    nums = list(map(int,input().split()))
    arr1.append(nums)
for i in range(int(col)):
    nums = list(map(int,input().split()))
    arr2.append(nums)
print()

for idx1 in range(len(arr1)):
    for idx2 in range(len(arr1[idx1])):
        print(arr1[idx1][idx2]*arr2[idx1][idx2], end="")
    print()