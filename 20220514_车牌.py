num=input("请输入车牌:")
i=len(num)
dan=["1","3","5","7","9"]
shuang=["0","2","4","6","8"]
while i != 0:
    i=i-1
    if num[i] in dan:
        print("单号")
        break
    elif num[i] in shuang:
        print("双号")
        break
