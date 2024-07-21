n = int(input('n='))
sum = 0 
# a,
for i in range (1, 2*n+2):
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
print(sum)
# b,
for i in range (1,n+1):
    sum += 1/i
print(sum)
# c,
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a == 0 : 
        if b == 0 : 
            if c == 0 : 
                print('phuong trinh vo so nghiem')
            else : 
                print('phuong trinh vo nghiem')
        else : 
            x = -c / b
            print('phuong trinh co 1 nghiem duy nhat : ', x)
else : 
        delta = b * b - 4 * a * c
        if delta < 0 : 
            print('phuong trinh vo nghiem')
        elif delta == 0 : 
            x = -b / (2 * a)
            print('phuong trinh co nghiem kep : ', x)
        else : 
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            print('phuong trinh co 2 nghiem phan biet :', x1, x2 )



