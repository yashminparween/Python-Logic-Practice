l1=[]
num=int(input("Enter the size="))
for i in range(0,num):
    n=int(input("enter the number="))
    l1.append(n)
largest_streak=1
current_streak=1
current_start=l1[0]
longest_start=l1[0]
previous=l1[0]
for i in range(1,num):
    if(previous<l1[1]):
        current_streak+=1
    else:
        if(current_streak>largest_streak):
            largest_streak=current_streak
            longest_start=current_start
        elif(current_streak==largest_streak):
            if(current_start<longest_start):
                longest_start=current_start

        current_streak=1
        current_start=l1[i]
    previous=l1[i]
if(current_streak>largest_streak):
    largest_streak=current_streak
    longest_start=current_start
elif(current_streak==largest_streak):
    if(current_start<longest_start):
        longest_start=current_start
print("Longest Streak",largest_streak)
print("Starting Number",longest_start)
    

    

        




        


    
    

    





    
    




        



