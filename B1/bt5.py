n = int(input('n ='))  
def tong_lap_phuong(n): 
    result=0   
    n_copy = n 
    while n_copy > 0:  
        r = int(n_copy%10)   
        result += r**3  
        n_copy = n_copy//10  
    return result  
for i in range (1,n+1): 
    if tong_lap_phuong(i) == i: 
        print(i,end=' ')  
