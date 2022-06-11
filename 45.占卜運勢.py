a = int(input())
b = int(input())
c = (a*2+b)%3
if c ==0:
    print("普通")
elif c==1:
    print("吉")
else:
    print("大吉")