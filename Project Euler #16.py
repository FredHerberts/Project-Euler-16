import time
start = time.time()
def Power_Digit_Sum(w,z):
    x = list(str(w))
    for y in x:
        z += int(y)
    print(z)

Power_Digit_Sum(2**1000,0)
end = time.time()
print(end - start)




