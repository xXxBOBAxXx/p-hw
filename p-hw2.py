from math import gcd

#222222222222222222222222222222222222222222222222 
n1, d1 = map(int, input('введите число "а/b": ').split('/'))
n2, d2 = map(int, input('введите число "а/b": ').split('/'))
 
if d1 == d2:
    print('{}/{}'.format(n1+n2, d1))
else:
    cd = int(d1*d2/gcd(d1, d2))
    rn = int(cd/d1*n1+cd/d2*n2)
    g2 = gcd(rn, cd)
    n = int(rn/g2)
    d = int(cd/g2)
    print('{}/{}'.format(n, d) if n != d else n)

#33333333333333333333333333333333333333333333333
num = int(input('введите число: '))
res = ''
sys = '0123456789ABCDEF'
 
while num > 0:
    res = sys[num % 16] + res
    num = num // 16 
print(res)