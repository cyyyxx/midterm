def prime(x):
    for i in range(2,x):
        if x % i ==0:
            return False
    return True
num = input("請輸入正整數:")
biggest = 0
for i in range (len(num)):
    for j in range(i,len(num)):
        is_prime= prime(int(num[i:j+1]))
        if is_prime and int(num[i:j+1])>biggest:biggest=int(num[i:j+1])
    if biggest: 
        print(f"子字串中最大的質數值為:{biggest}")
    else:
        print("No primw found")
