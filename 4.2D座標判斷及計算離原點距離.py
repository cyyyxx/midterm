def z(x,y,z,c):
    if b >0:
        print("該點位於{}離原點距離為根號{}".format(x,c))
    elif b<0:
        print("該點位於%s離原點距離為根號%.2f"%(y,c))   
    else:
        print(f"該點位於{z}離原點距離為根號{c}")
a = int(input("請輸入x座標"))
b = int(input("請輸入y座標"))
c = (a**2+b**2)
if a>0:
    z('第一象限','第四象限','右半平面',c)
elif a<0:
    z('第二象限','第三象限','左半平面',c)
else:
    z('上半平面','下半平面','原點',c)
