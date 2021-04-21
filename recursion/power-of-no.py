def powerofno(num,power):

    if power==0 or power==1:
        return num
    else:
        return (num*powerofno(num,power-1))

print(powerofno(5,2))
