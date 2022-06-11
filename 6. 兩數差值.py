min = ""
max = ""
input_value = input("Give me number!!(x,y,z)")
input_value = input_value.split(",")
input_value.sort()
minInput_Value = input_value
print(minInput_Value)
for I in minInput_Value:
    min+=str(I)
input_value.reverse()
maxInput_Value = input_value
print(maxInput_Value)
for i in maxInput_Value:
    max+=str(i)

answer =int(max)-int(min)
print("最大值數列與最小值數列差值為:",answer)
