def powerofno(num,power):

    if power==0:
        return 1
    elif power==1:
        return num
    else:
        return (num*powerofno(num,power-1))

print(powerofno(5,0))
