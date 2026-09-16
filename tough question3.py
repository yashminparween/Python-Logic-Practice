l1=[]
l2=[]
num=int(input("enter the number="))
for i in range(1,num+1):
    temp=i
    while(temp!=0):
        digit=temp%10
        l1.append(digit)
        temp=temp//10
print(l1)
for i in range(0,10):
    count=0
    for j in l1:
        if (i==j):
            count+=1
    l2.append([i,count])
print(l2)
def is_prime(num):
    if(num<=1):
        return False
    for i in range(2,int(num**0.5)+1):
        if (num%i==0):
            return False
    return True
count_prime=0
count_nonprime=0
for index,value in enumerate (l2):
    if is_prime(l2[index][0]):
        count_prime+=l2[index][1]
    else:
        count_nonprime+=l2[index][1]
print("The total count of prime number",count_prime)
print("The total count of non prime number",count_nonprime)
largest=l2[0][1]
largest_digit=l2[0][0]
for index,value in enumerate(l2):
    if(l2[index][1]>largest):
        largest=l2[index][1]
        largest_digit=l2[index][0]
    elif(l2[index][1]==largest) and (l2[index][0]<largest_digit):
        largest_digit=l2[index][0]


print("the largest frequency is",largest)
print("the largest frequency digit is",largest_digit)
        
    

    




    
































































