l1=[]
l2=[]
n=int(input("enter the size="))
for i in range(0,n):
    num=int(input("Enter the number="))
    l1.append(num)
for i in l1:
    if(i not in l2):
        l2.append(i)
largest=l2[0]
for i in l2:
    if(largest<i):
        largest=i
count=0
second_largest=""
for i in l2:
    count+=1
found=False
if(count==1):
    print("\nSecond largest number doesn't exist")

elif(count==2):
    for i in l2:
        if(largest==i):
            print("")
        else:
            second_largest=i
            found=True
else:
    second_largest=l2[0]
    for i in l2:
        if(i>second_largest) and (largest!=i):
                second_largest=i
                Found=True
print(f"\nThe largest number is {largest}\n")
if (found==True):
    print(f"The second largest number is {second_largest}")





