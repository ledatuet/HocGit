def nhap(n):
    a = str(n)
    l = len(a)
    for i in range(0,l//2):
        if a[i] != a[l-1-i]:
            return False
        return True
def nguoc(n):
    k = 0
    while n > 0:
        k = k*10 + n%10
        n //= 10
    return k
n = int(input())
k = 0
while n < 10000:
    if nhap(n):
        print(k,n)
    n = n+nguoc(n)
    k += 1