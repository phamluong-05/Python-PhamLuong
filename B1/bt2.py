#Bài 2:
a=int(input('a='))
b=int(input('b='))
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}**{b}={a**b}')
if b != 0:
    print(f'{a}//{b}={a//b}')
    print(f'{a}%{b}={a%b}')
else: 
    print('khong the thuc hien phep chia')
def so_sanh(a,b):
    if a>b:
        return f'{a}>{b}'
    elif a<b:
        return f'{a}<{b}'
    else: 
        return f'{a}={b}'
print(so_sanh(a,b))
print(a and b)
print(a or b)
print(a ^ b)
print(not a == b)
print(a >> 1)
print(a << 1)