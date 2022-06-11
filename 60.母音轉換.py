a = input("請輸入一串小寫英文:")
b= ["a", "e", "i", "o", "u"]
ans = ""
for char in a:
    if char in b: a = a.replace(char, ".")
print(a)