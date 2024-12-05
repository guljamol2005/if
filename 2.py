for i in range(100, 1000):
    num=i
    yuzlik = num//100
    onlik = (num//10)%10
    birlik =num%10
    if(yuzlik==onlik or onlik==birlik or yuzlik==birlik):
        print(num)       
3
