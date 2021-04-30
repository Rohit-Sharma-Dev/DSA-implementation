
def rec(n):
    # num=0/
    if n==1:
        return 1
    return n+rec(n-1)
print(rec(4))

# ----------simple recursion as given in the sheet

def one(n):
    if n>0:
        one(n-1)
    print(n)

one(5)
