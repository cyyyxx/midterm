a = ("紅豆生南國,春來發幾枝?願君多采擷,此物最相思。")
b = ("春眠不覺曉,處處聞啼鳥,夜來風雨聲,花落知多少。")
n = []
for i in a:
    if i != "," and i != "。" and i in b and i not in n:
        n.append(i)
print(n)