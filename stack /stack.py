
def createstack():
    stack=[]
    return stack

def isEmpty():
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    return stack

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)
    
    return stack.pop()


stack=createstack()
push(stack,str(10))
push(stack,12)
pop(stack)
print(stack)



# import 
class revstring:
    def __init__(self):
        self.container=[]

    
    def reverse (value):
        b=''
        for i in range(len(value)):
            b+=value[len(value)-1-i]
        return b 

print(revstring.reverse("rohit"))










usr="rohit"
usr1=""
for i in range(len(usr)):
    usr1+=usr[len(usr)-1-i]

print(usr1)