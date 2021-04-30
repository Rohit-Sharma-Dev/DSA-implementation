def ncr(n,r):
    return (fact(n)//(fact(r)*fact(n-r)))

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

# ncr(5,2)
print(ncr(5,2))
