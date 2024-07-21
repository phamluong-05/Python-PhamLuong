n = int(input('nhập n: '))
def tong_cua_uoc(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total
for i in range(1, n + 1):
    sum = tong_cua_uoc(i)
    if tong_cua_uoc(i) == i and sum < i:
        print(i, sum)