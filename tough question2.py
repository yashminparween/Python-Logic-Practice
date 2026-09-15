def is_prime(num):
    if(num<=1):
        return False
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
    return True
num=int(input("enter a number="))
sum_prime=0
sum_nonprime=0
for i in range(1,num+1):
      temp=i
      while(temp!=0):
         digit=temp%10
         if is_prime(digit):
             sum_prime+=digit
         else:
             sum_nonprime+=digit
             
        
         temp=temp//10
print(sum_prime)
print(sum_nonprime)
if(sum_prime>sum_nonprime):
    print("the sum of prime digit",sum_prime)
    difference=sum_prime-sum_nonprime
    print(difference)


