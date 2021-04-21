def sumofn(n):
    if n==1:
        return 1
    return n+sumofn(n-1)

print(sumofn(6))