year = int(input("請輸入西元年"))
animal = {0:"monkey",1:"rooster",2:"dog",3:"pig",4:"rat",5:"ox",6:"tiger",7:"rabbit",8:"dragon",9:"snake",10:"hourse",11:"sheep"}
a = year%12
print("%d年是%s"%(year,animal[a]))