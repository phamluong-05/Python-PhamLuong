n=int(input('n ='))
def tong_cua_uoc(n):
    sum=0
    for i in range(1,(int)(n/2)+1):
        if n%i==0:
            sum += i
    return sum
for i in range (1, n+1):
    if tong_cua_uoc(i) == i:
        print(i, end=' ')