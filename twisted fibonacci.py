
def isprime(number):
    for i in range(2,number):
       if (number % i) == 0:
           return False
       else:
           return True
num = int(input())
a=0
b=1
list = []
for i in range(0,num):
    c=a+b
    list.append(c)
    a=b
    b=c
print(list)
for index, elem in enumerate(list):
    if isprime(elem) == True:
        list[index]=0
print(list)
        
