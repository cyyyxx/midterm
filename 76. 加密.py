a = list(input("請輸入傳送密碼(六位數):"))
b = ''
for i in a:
    for j in range(10):
        if j*4%7 == int(i):
            b += str(j)
            break
print("解密後的密碼:",b)