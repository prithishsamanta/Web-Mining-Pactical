from math import log, ceil
log2 = lambda x: log(x, 2)
def binary(x, l=1):
    fmt = '{0:0%db}' % l
    return fmt.format(x)
def unary(x):
    return (x-1)*'0'+'1'
def golomb(b, x):
    q = int((x) / b)
    r = int((x) % b)
    l = int(ceil(log2(b)))
    #print q,r,l
    print('q = ', q, ' r = ', 'l = ', l)
    return unary(q) + binary(r, l)
n = int(input("Enter a no for which you want to calculate  Golomb (b = 10): "))
print(golomb(10, n))
