item = ""
ans = []
while item != "end":
    item = input("請輸入事項(若已無事項，請輸入 end):")
    ans.append(item)

for i in ans[:-1]:
    print(f"{ans.index(i)+1}. {i}")