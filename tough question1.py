
def is_prime(num):
    if(num<=1):
        return False
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
    return True
n=int(input("enter the number="))
for i in range(1,n+1):
    if(i<10):
        if is_prime(i):
            print(i)
    else:
        temp=i
        digit_sum=0
        while(temp!=0):
            digit=temp%10
            digit_sum+=digit
            temp=temp//10
        if is_prime(digit_sum):
            print(i)

    
        
           
            



            