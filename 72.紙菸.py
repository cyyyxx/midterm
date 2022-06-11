a = int(input("請輸入n: "))
b = int(input("請輸入k: "))
add = a // b
total = add
while add >= b:
    add //= b
    total += add
print(f"Peter 可以抽 {a+total} 支紙菸")