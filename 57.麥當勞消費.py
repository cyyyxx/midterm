dict = {"1":72,"2":62,"3":82,"4":44,"5":60,"A":55,"B":68}
set = list(input("請選擇主餐及升級的套餐:"))
drink = input("是否升級成大杯飲料:")
chip = input("是否換成大薯:")
money = 0
if len(set) > 1:
    money += dict[set[0]] + dict[set[1]]
else:
    money += dict[set[0]]
if drink == "是":
    money += 7
if chip == "是":
    money += 13
print("總共為%d元" %(money))