import time

def ajaibrekur(x):
    if x <=5 :
        return x
    else:
        return ajaibrekur(x-2)+ajaibrekur(x//2)






def ajaibitera(x):
    hasil =[1,2,3,4,5]
    for i in range(5,):
        y = hasil[x-3]

        hasil.append(y)
    print(hasil)
ajaibitera(10)

start = time.time()
print(ajaibrekur(10))
end = time.time()

print(end-start)