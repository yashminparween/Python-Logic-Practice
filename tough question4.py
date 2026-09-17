l1=[]
l2=[]
n=int(input("enter the size="))
for i in range(1,n+1):
    num=int(input("enter the number"))
    count=0
    temp=num
    previous_digit=num%10
    while(temp!=0):
        digit=temp%10
        if(digit==previous_digit): 
            count+=1
            previous_digit=digit
        else:
           l1.append([previous_digit,count])
           count=1
           previous_digit=digit
        temp=temp//10
    l1.append([previous_digit,count])
for digit,count in l1:
    found=False
    for item in l2:
        if item[0]==digit:
            item[1]=item[1]+count
            found=True
            break
        
    if found==False:
            l2.append([digit,count])
print(l2)

            

        

        



